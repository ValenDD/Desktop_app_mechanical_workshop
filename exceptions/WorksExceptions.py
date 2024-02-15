class WorkExistException(Exception):
    def __init__(self, message):
        super().__init__(message)
        
class WorkNotExistException(Exception):
    def __init__(self, message):
        super().__init__(message)