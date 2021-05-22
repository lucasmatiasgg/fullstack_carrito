from json import JSONEncoder

class EntityResponse:
    errorCode = 0
    message = ''
    success = False

    def __init__(self, errorCode, message, success):
        self.errorCode = errorCode
        self.message = message
        self.success = success

    def __str__(self):
        return self.errorCode + ' - ' + self.message

# subclass JSONEncoder
class EntityResponseEncoder(JSONEncoder):
        def default(self, obj):
            return obj.__dict__