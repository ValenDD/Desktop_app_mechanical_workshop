from models import work
from exceptions import exceptions

class WorkController:
    _instance = None
    _factory = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(WorkController, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        from utils.Factory import Factory
        if not hasattr(self, 'is_initialized'):
            self.is_initialized = True
            self.factory = Factory()
            
    def create_work(self, date_in, date_out, client_name, vehicle, diagnosis, repair, spare_part_cost, repair_cost, total_price, payment_method, done):
        try:
            self.client_controller = self.factory.get_controller('clientController')
            client = self.client_controller.find_users(client_name)
            new_work = work.Work(client, date_in, date_out, client_name, vehicle, diagnosis, repair, spare_part_cost, repair_cost, total_price, payment_method, done)
            work_dao = self.factory.get_controller('DAOcontroller')
            client_id = self.client_controller.client_id(client_name)
            work_dao.saveWork(client_id, new_work)
        except exceptions.ClientNotExistException as e:
            raise exceptions.ClientNotExistException(e)
        
    def list_works(self):
        work_dao = self.factory.get_controller('DAOcontroller')
        return work_dao.listWorks()
    
    def search_client_works(self, client_name):
        work_dao = self.factory.get_controller('DAOcontroller')
        return work_dao.searchClientWorks(client_name)