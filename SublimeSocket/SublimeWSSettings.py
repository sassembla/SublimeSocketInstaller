SS_HOST_REPLACE = "SUBLIMESOCKET_HOST"
SS_PORT_REPLACE = "SUBLIMESOCKET_PORT"
SS_VERSION_REPLACE = "SUBLIMESOCKET_VERSION"


#Protocole version	see-> http://tools.ietf.org/html/rfc6455
VERSION = 13

#Operation codes
OP_CONTINUATION = 0x0
OP_TEXT = 0x1
OP_BINARY = 0x2
OP_CLOSE = 0x8
OP_PING = 0x9
OP_PONG = 0xA

OPCODES = (OP_CONTINUATION, OP_TEXT, OP_BINARY, OP_CLOSE, OP_PING, OP_PONG)