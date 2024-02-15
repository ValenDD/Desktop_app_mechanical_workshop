from models import client
from exceptions.ClientExceptions import ClientExistException
from exceptions.ClientExceptions import ClientNotExistException
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
        if not self.client_exists(name):
            new_client = client.Client(name, phone)
            client_dao = self.factory.get_controller('DAOcontroller')
            client_dao.saveClient(new_client)
        else:
            raise ClientExistException("El cliente ya existe")
            
    def list_clients(self):
        client_dao = self.factory.get_controller('DAOcontroller')
        return client_dao.listClients()
    
    def list_client_only_name(self):
        client_dao = self.factory.get_controller('DAOcontroller')
        return client_dao.listClientOnlyName()
        
    def client_exists(self, name):
        client_dao = self.factory.get_controller('DAOcontroller')
        return client_dao.clientExists(name)

    def find_users(self, name):
        client_dao = self.factory.get_controller('DAOcontroller')
        if client_dao.clientExists(name):
            return client_dao.findClients(name)
        else:
            raise ClientNotExistException("El cliente no existe")
        
    def update_client_name(self, name, new_name, new_phone):
        if self.client_exists(name):
            client_dao = self.factory.get_controller('DAOcontroller')
            client_dao.updateClientName(name, new_name, new_phone)
        else:
            raise ClientNotExistException("El cliente no existe")
    
    def client_id(self, name):
        client_dao = self.factory.get_controller('DAOcontroller')
        return client_dao.client_id(name)
        
    def delete_client(self, name):
        if self.client_exists(name):
            client_dao = self.factory.get_controller('DAOcontroller')
            client_dao.deleteClient(name)
        else:
            raise ClientNotExistException("El cliente no existe")