from dao.clientDAO import ClientDAO
from dotenv import load_dotenv
import os

class ClientDAO_Controller:
    _instance = None
    _factory = None
    dbconfig = {}

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ClientDAO_Controller, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        from utils.Factory import Factory
        if not hasattr(self, 'is_initialized'):
            self.is_initialized = True
            self.factory = Factory()

    def saveClient(self, client):
        client_dao = ClientDAO(self.set_dbconfig())
        client_dao.save(client)
        client_dao.close_conection()

    def set_dbconfig(dbconfig):
        load_dotenv()
        dbconfig = {
            'dbname': os.getenv('DB_NAME'),
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'host': os.getenv('DB_HOST'),
            'port': os.getenv('DB_PORT')
        }
        return dbconfig
    
    def listClients(self):
        client_dao = ClientDAO(self.set_dbconfig())
        clients = client_dao.list()
        client_dao.close_conection()
        return clients
    
    def clientExists(self, phone):
        client_dao = ClientDAO(self.set_dbconfig())
        client = client_dao.client_exists(phone)
        client_dao.close_conection()
        return client