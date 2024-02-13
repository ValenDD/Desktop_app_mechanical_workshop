from models import client
import os
from dotenv import load_dotenv

class ClientController:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ClientController, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'is_initialized'):
            self.is_initialized = True

    def create_user(self, name, phone):
        from utils.Factory import Factory
        new_client = client.Client(name, phone)
        self.factory = Factory()
        client_dao = self.factory.get_controller('clientDAO')
        client_dao.saveClient(new_client)