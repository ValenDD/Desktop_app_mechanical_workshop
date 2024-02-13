from dao.clientDAO import ClientDAO
from dotenv import load_dotenv
import os

class ClientDAO_Controller:
    _instance = None
    dbconfig = {}
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ClientDAO_Controller, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'is_initialized'):
            self.is_initialized = True

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