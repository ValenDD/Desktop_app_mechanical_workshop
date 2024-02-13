from models import client
from exceptions.exceptions import ClientExistException
class ClientController:
    _instance = None
    _factory = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ClientController, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        from utils.Factory import Factory
        if not hasattr(self, 'is_initialized'):
            self.is_initialized = True
        self.factory = Factory()

    def create_user(self, name, phone):
        if not self.client_exists(phone):
            new_client = client.Client(name, phone)
            client_dao = self.factory.get_controller('clientDAO')
            client_dao.saveClient(new_client)
        else:
            raise ClientExistException("El cliente ya existe")
            
    def list_clients(self):
        client_dao = self.factory.get_controller('clientDAO')
        return client_dao.listClients()
    
    def client_exists(self, phone):
        client_dao = self.factory.get_controller('clientDAO')
        return client_dao.clientExists(phone)
