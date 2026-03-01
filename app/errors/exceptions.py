class ContactValidationError(Exception):
    def __init__(self, message, errors=None):
        super().__init__(message)
        self.errors = errors or []

class RateLimitExceededError(Exception):
    def __init__(self, message="Rate limit exceeded"):
        super().__init__(message)

class ExternalServiceError(Exception):
    def __init__(self, message="External service unavailable"):
        super().__init__(message)
