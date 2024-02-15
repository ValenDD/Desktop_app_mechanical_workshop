class ClientExistException(Exception):
    def __init__(self, message):
        super().__init__(message)
        
class ClientNotExistException(Exception):
    def __init__(self, message):
        super().__init__(message)