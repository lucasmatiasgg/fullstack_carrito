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