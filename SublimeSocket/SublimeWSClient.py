# -*- coding: utf-8 -*-
import sublime, sublime_plugin

import threading, hashlib, base64
import SublimeWSSettings

from SublimeWSDecoder import SublimeWSDecoder

from SublimeWSController import SublimeWSController


class SublimeWSClient:
	CONNECTION_STATUS = {
		'CONNECTING': 0x0,
		'OPEN': 0x1,
		'CLOSING': 0x2,
		'CLOSED': 0x3
	}

	## Constructor
	#  @param server WebSocket Server object attached to client.
	def __init__(self, server, identity):
		self.server = server
		self.conn = ''
		self.addr = ''
		self.setStatus('CLOSED')
		self.cont = SublimeWSController(self)
		self.clientId = identity


	## Set current connection status
	#  @param status Status of the socket. Can be 'CONNECTING', 'OPEN', 'CLOSING' or 'CLOSED'.
	def setStatus(self, status=''):
		if (status in self.CONNECTION_STATUS):
			self.status = self.CONNECTION_STATUS[status]

	## Test current connection status
	#  @param status Status of the socket. Can be 'CONNECTING', 'OPEN', 'CLOSING' or 'CLOSED'.
	def hasStatus(self, status):
		if (status in self.CONNECTION_STATUS):
			return self.status == self.CONNECTION_STATUS[status]
		return False

	## Real socket bytes reception
	#  @param bufsize Buffer size to return.
	def receive(self, bufsize):
		
		bytes = self.conn.recv(bufsize)
		if not bytes:
			closingMessage = self.clientId + " left from SublimeSocket. because they send 'no-bytes'"

			print "ss:", closingMessage
			sublime.set_timeout(lambda: sublime.status_message(closingMessage), 0)

			self.close()
			self.server.deleteClientId(self.clientId)
			return ''
		return bytes

	## Try to read an amount bytes
	#  @param bufsize Buffer size to fill.
	def read(self, bufsize):
		remaining = bufsize
		bytes = ''
		while remaining and self.hasStatus('OPEN'):
			bytes += self.receive(remaining)
			remaining = bufsize - len(bytes)
		return bytes

	## Read data until line return (used by handshake)
	def readlineheader(self):
		line = []
		while self.hasStatus('CONNECTING') and len(line)<1024:
			c = self.receive(1)
			line.append(c)
			# print 'readlineheader: ', line
			if c == "\n":
				break
		return "".join(line)

	## Send handshake according to RFC
	def handshake(self):
		headers = {}
		
		# Ignore first line with GET
		line = self.readlineheader()
		while self.hasStatus('CONNECTING'):
			if len(headers)>64:
				raise ValueError('Header too long.')
			line = self.readlineheader()
			if not self.hasStatus('CONNECTING'):
				raise ValueError('Client left.')
			if len(line) == 0 or len(line) == 1024:
				raise ValueError('Invalid line in header.')
			if line == '\r\n':
				break
			
			# take care with strip !
			# >>> import string;string.whitespace
			# '\t\n\x0b\x0c\r '
			
			line = line.strip()

			# take care with split !
			# >>> a='key1:value1:key2:value2';a.split(':',1)
			# ['key1', 'value1:key2:value2']
			
			kv = line.split(':', 1)
			if len(kv) == 2:
				key, value = kv
				k = key.strip().lower()
				v = value.strip()
				headers[k] = v
			else:
				raise ValueError('Invalid header key/value.')
		
		#print headers
		if not len(headers):
			raise ValueError('Reading headers failed.')
		if not 'sec-websocket-version' in headers:
			raise ValueError('Missing parameter "Sec-WebSocket-Version".')
		if not 'sec-websocket-key' in headers:
			raise ValueError('Missing parameter "Sec-WebSocket-Key".')
		if not 'host' in headers:
			raise ValueError('Missing parameter "Host".')
		if not 'origin' in headers:
			raise ValueError('Missing parameter "Origin".')

		if (int(headers['sec-websocket-version']) != SublimeWSSettings.VERSION):
			raise ValueError('Wrong protocol version %s.' % SublimeWSSettings.VERSION)

		accept = base64.b64encode(hashlib.sha1(headers['sec-websocket-key'] + '258EAFA5-E914-47DA-95CA-C5AB0DC85B11').digest())

		bytes = ('HTTP/1.1 101 Switching Protocols\r\n'
			'Upgrade: websocket\r\n'
			'Connection: Upgrade\r\n'
			'Sec-WebSocket-Origin: %s\r\n'
			'Sec-WebSocket-Location: ws://%s\r\n'
			'Sec-WebSocket-Accept: %s\r\n'
			'Sec-WebSocket-Version: %s\r\n'
			'\r\n') % (headers['origin'], headers['host'], accept, headers['sec-websocket-version'])

		handshakeMessage = '--- HANDSHAKE ---\r\n'
		handshakeMessage = handshakeMessage + '-----------------\r\n'
		handshakeMessage = handshakeMessage + bytes + '\r\n'
		handshakeMessage = handshakeMessage + '-----------------\r\n'
		

		sublime.set_timeout(lambda: sublime.status_message("handshaking.."), 0)
		
		self.send(bytes)

	## Handle incoming datas
	#  @param conn Socket of WebSocket client (from WSServer).
	#  @param addr Adress of WebSocket client (from WSServer).
	def handle(self, conn, addr):
		self.conn = conn
		self.addr = addr
		self.setStatus('CONNECTING')
		try:
			self.handshake()
		except ValueError as error:
			self.close()
			self.server.deleteClientId(self.clientId)
			raise ValueError('Client rejected: ' + str(error))
		else:
			decoder = SublimeWSDecoder()
			self.setStatus('OPEN')
			while self.hasStatus('OPEN'):
				try:
					(ctrl, data) = decoder.decode(self)
				except ValueError as (closing_code, message):
					if self.hasStatus('OPEN'):
						print "there is no kill yet.", closing_code, message
						# self.cont.kill(closing_code,'WSDecoder::'+str(message))
					break
				else:
					self.cont.run(ctrl, data)

	## Send an unicast frame
	#  @param bytes Bytes to send.
	def send(self, bytes):
		if not self.hasStatus('CLOSED'):
			# print 'SEND TO:', self.clientId, "/via", repr(self.conn), repr(bytes), '[', str(len(bytes)), ']'
			lock = threading.Lock()
			lock.acquire()
			self.conn.send(bytes)
			lock.release()

	## Close connection (don't forget to remove client from WebSocket Server first !)
	def close(self):
		if not self.hasStatus('CLOSED'):
			self.setStatus('CLOSED')
			self.conn.close()


