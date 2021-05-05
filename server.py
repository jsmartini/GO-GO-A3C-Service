from starlette.applications import Starlette
from starlette.responses import Fileresponses, Response
from starlette.requests import Request
from starlette.routing import Route

class GlobalNet:

    WBUFFER = {}    #weight buffer
    WORKERS = []    #workers connected

    def __init__(self, port):
