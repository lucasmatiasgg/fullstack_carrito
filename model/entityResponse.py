import json
from json import JSONEncoder

class EntityResponse:
    errorCode = 0
    message = ''
    success = False

    def __init__(self, errorCode, message, success):
        self.errorCode = errorCode
        self.message = message
        self.success = success

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

# subclass JSONEncoder
class EntityResponseEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__