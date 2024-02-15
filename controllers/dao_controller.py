from dao.clientDAO import ClientDAO
from dao.workDAO import WorkDAO
from dotenv import load_dotenv
import os

class DAOcontroller:
    _instance = None
    _factory = None
    dbconfig = {}

#Settings
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DAOcontroller, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        from utils.Factory import Factory
        if not hasattr(self, 'is_initialized'):
            self.is_initialized = True
            self.factory = Factory()
    
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
            
#ClientDAO
    def saveClient(self, client):
        client_dao = ClientDAO(self.set_dbconfig())
        client_dao.save(client)
        client_dao.close_conection()
    
    def listClients(self):
        client_dao = ClientDAO(self.set_dbconfig())
        clients = client_dao.list()
        client_dao.close_conection()
        return clients
    
    def listClientOnlyName(self):
        client_dao = ClientDAO(self.set_dbconfig())
        clients = client_dao.list_only_name()
        client_dao.close_conection()
        return clients
    
    def clientExists(self, name):
        client_dao = ClientDAO(self.set_dbconfig())
        client = client_dao.client_exists(name)
        client_dao.close_conection()
        return client
    
    def findClients(self, name):
        client_dao = ClientDAO(self.set_dbconfig())
        clients = client_dao.find(name)
        client_dao.close_conection()
        return clients
    
    def updateClientName(self, name, new_name, new_phone):
        client_dao = ClientDAO(self.set_dbconfig())
        client_dao.update(name, new_name, new_phone)
        client_dao.close_conection()
    
    def deleteClient(self, name):
        client_dao = ClientDAO(self.set_dbconfig())
        client_dao.delete(name)
        client_dao.close_conection()
        
#WorkDAO
    def saveWork(self, work):
        work_dao = WorkDAO(self.set_dbconfig())
        work_dao.save(work)
        work_dao.close_conection()


