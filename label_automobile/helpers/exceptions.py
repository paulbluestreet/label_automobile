
class NotFoundError(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors


class AuthorizationError(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors
