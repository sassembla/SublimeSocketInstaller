
#API for Input to ST2 through WebSocket

### COMMAND		=		COMMAND_NAME : JSON_EXPRESSION
### COMMANDS	=		COMMAND_NAME : JSON_EXPRESSION -> COMMAND_NAME : JSON_EXPRESSION -> ...
### COMMANDS	=		COMMAND_NAME + COMMAND_NAME : JSON_EXPRESSION -> COMMAND_NAME + COMMAND_NAME + COMMAND_NAME : JSON_EXPRESSION -> ...

API_PREFIX = "sublimesocket"

API_PREFIX_SUB = "ss"
API_DEFINE_DELIM = "@"					# sublimesocket@commandA:{}->commandB:{}->commandC:[]->
API_CONCAT_DELIM = "->"					# concat commands. every commands run in sequential.
API_COMMAND_PARAMS_DELIM = ":"	# only first ":" will be evaluated as delimiter / each commnand.

API_COMMENT_DELIM	= "/"					# comment expression in API. ss@COMMENT/API...

API_PARAM_START		= "("					# ss@(key|value,key2|value2)commandA:,,,
API_PARAM_END			= ")"					# replace commandA's "key" by "value" of present-results.
API_PARAM_CONCAT	= "|"
API_PARAM_DELIM		= ","


API_VERSION = "1.0.1"
SOCKET_VERSION = 2	# for Sublime Text 2

# SublimeSocket internal event definition
SS_EVENT_COLLECT	= "ss_collect"

SS_FOUNDATION_NOVIEWFOUND	= "ss_f_noViewFound"
NOVIEWFOUND_TARGET		= "target"
NOVIEWFOUND_VIEW			= "view"
NOVIEWFOUND_LINE			= "line"
NOVIEWFOUND_MESSAGE		= "message"
NOVIEWFOUND_CONDITION = "condition"


SS_FOUNDATION_RUNWITHBUFFER = "ss_f_runWithBuffer"
F_RUNWITHBUFFER_TARGET	= "target"
F_RUNWITHBUFFER_VIEW		= "view"
F_RUNWITHBUFFER_BODY		= "body"
F_RUNWITHBUFFER_PATH		= "path"
SIZE_OF_BUFFER					= 100000


# internal APIs/
API_I_SHOWSTATUSMESSAGE	= "showStatusMessage"
SHOWSTATUSMESSAGE_MESSAGE	= "message"

API_I_ERASEALLREGION	= "eraseAllRegion"

# /internal APIs

# region identifier prefix
REGION_UUID_PREFIX = "ss_"


# public APIs
API_VERSIONVERIFY	= "versionVerify"
VERSIONVERIFY_SOCKETVERSION	= "socketVersion"
VERSIONVERIFY_APIVERSION		= "apiVersion"


API_RUNSETTING		= "runSetting"
RUNSETTING_FILEPATH	= "path"
RUNSETTING_PREFIX_SUBLIMESOCKET_PATH = "SUBLIMESOCKET_PATH:"

API_INPUTIDENTITY = "inputIdentity"
IDENTITY_ID				= "id"

API_TEARDOWN			=	"tearDown"

API_SETREACTOR		= "setReactor"
REACTOR_TARGET		= "target"
REACTOR_EVENT			= "event"
REACTOR_SELECTORS	= "selectors"
REACTOR_INTERVAL	= "interval"
REACTOR_REPLACEFROMTO		= "replacefromto"
REACTOR_VIEWKEY_VIEWSELF	= "view"
REACTOR_VIEWKEY_ID				= "viewId"
REACTOR_VIEWKEY_BUFFERID	= "bufferId"
REACTOR_VIEWKEY_PATH			= "path"
REACTOR_VIEWKEY_BASENAME	= "basename"
REACTOR_VIEWKEY_VNAME			= "vname"

API_SETFOUNDATIONREACTOR			= "setFoundationReactor"
FOUNDATIONREACTOR_EVENT				= "event"
FOUNDATIONREACTOR_SELECTORS		= "selectors"
FOUNDATIONREACTOR_TARGET_DEFAULT 		= "default"
FOUNDATIONREACTOR_INTERVAL_DEFAULT	= 0

REACTIVE_RESERVED_INTERVAL_EVENT	= ["on_modified", "on_selection_modified", "on_pre_save", "on_post_save"]
REACTIVE_PREFIX_USERDEFINED_EVENT	= "event_"
REACTIVE_FOUNDATION_EVENT = [SS_FOUNDATION_NOVIEWFOUND, SS_FOUNDATION_RUNWITHBUFFER]

API_KEYVALUESTORE	= "kvs"
KVS_SHOWALL				= "showAll"
KVS_SHOWVALUE			= "showValue"
KVS_REMOVEVALUE		= "removeValue"
KVS_CLEAR					= "clear"

API_DEFINEFILTER	= "defineFilter"
DEFINEFILTER_PATTERNS		= "patterns"
DEFINEFILTER_NAME = "name"


API_FILTERING			= "filtering"
FILTER_NAME				= "name"
FILTER_SOURCE			= "source"
FILTER_SELECTORS	= "selectors"
FILTER_DEBUG			= "debug"

API_CONTAINSREGIONS	= "containsRegions"
CONTAINSREGIONS_VIEW	= "view"
CONTAINSREGIONS_TARGET	= "target"
CONTAINSREGIONS_EMIT	= "emit"
CONTAINSREGIONS_DEBUG	= "debug"

API_COLLECTVIEWS	= "collectViews"

API_RUNSHELL			= "runShell"
RUNSHELL_MAIN			= "main"
RUNSHELL_DELAY		= "delay"
RUNSHELL_DEBUG		= "debug"
RUNSHELL_LIST_IGNORES = [RUNSHELL_MAIN, RUNSHELL_DELAY, RUNSHELL_DEBUG]
RUNSHELL_REPLACE_SPACE	= "_"
RUNSHELL_REPLACE_RIGHTBRACE = ""
RUNSHELL_REPLACE_LEFTBRACE	= ""
RUNSHELL_REPLACE_At_s_At_s_At			= " "


API_BROADCASTMESSAGE	= "broadcastMessage"
API_MONOCASTMESSAGE		= "monocastMessage"
OUTPUT_TARGET			= "target"
OUTPUT_MESSAGE		= "message"
OUTPUT_DELIMITER	= "delimiter"
OUTPUT_HEADER			= "header"
OUTPUT_FOOTER			= "footer"
OUTPUT_SENDER			= "sender"

API_SHOWATLOG			= "showAtLog"
LOG_MESSAGE				= "message"
LOG_prefix				= "ss:"

API_APPENDREGION	= "appendRegion"
APPENDREGION_VIEW	= "view"
APPENDREGION_LINE	= "line"
APPENDREGION_MESSAGE	= "message"
APPENDREGION_CONDITION = "condition"

API_RUNWITHBUFFER	= "runWithBuffer"
RUNWITHBUFFER_VIEW = "view"

API_NOTIFY				= "notify"
NOTIFY_TITLE			= "title"
NOTIFY_MESSAGE		= "message"
NOTIFY_DEBUG			= "debug"

API_GETALLFILEPATH	= "getAllFilePath"
GETALLFILEPATH_PATHS = "paths"
GETALLFILEPATH_ANCHOR = "anchor"
GETALLFILEPATH_HEADER	= "header"
GETALLFILEPATH_FOOTER	= "footer"

API_READFILEDATA	= "readFileData"
READFILEDATA_PATH = "path"
READFILEDATA_DATA = "data"

API_EVENTEMIT			= "eventEmit"
EVENTEMIT_TARGET	= "target"
EVENTEMIT_EVENT		= "event"

API_SETWINDOWBASEPATH = "setWindowBasePath"

API_TIMEREVENT		= "timerEvent"

API_EVAL					= "eval"


#Dictionaries for collection of "Views", "filters", "events"
DICT_VIEWS				= "DICT_VIEWS"

VIEW_PATH					= "path"
VIEW_ID						= "viewId"
VIEW_BUFFERID			= "bufferId"
VIEW_BASENAME			= "basename"
VIEW_VNAME				= "vname"
VIEW_SELF					= "view"

VIEW_EVENTS_RENEW	= ["on_new", "on_clone", "on_load", "on_modified", SS_EVENT_COLLECT] #list of acceptable-view renew event names.
VIEW_EVENTS_DEL		= ["on_close"] #list of acceptable-view del event names.


DICT_FILTERS			= "DICT_FILTERS"


DICT_REACTORS			= "DICT_REACTORS"


SUBDICT_REGIONS		= "SUBDICT_REGIONS"
REGION_IDENTITY		= "identity"
REGION_SELF				= "region"
REGION_EVENT			= "event"
REGION_MESSAGE		= "message"
REGION_LINE				= "line"

SUBARRAY_DELETED_REGIONS		= "SUBARRAY_DELETED_REGIONS"


