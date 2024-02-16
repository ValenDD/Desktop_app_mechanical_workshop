from models import work
from exceptions import ClientExceptions
from exceptions import WorksExceptions
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
        except ClientExceptions.ClientNotExistException as e:
            raise ClientExceptions.ClientNotExistException(e)
        
    def list_works(self):
        work_dao = self.factory.get_controller('DAOcontroller')
        return work_dao.listWorks()
    
    def search_client_works(self, client_name):
        work_dao = self.factory.get_controller('DAOcontroller')
        return work_dao.searchClientWorks(client_name)
    
    def update_work(self, work_id, date_in, date_out, client_name, vehicle, diagnosis, repair, spare_part_cost, repair_cost, total_price, payment_method, done):
        try:
            work_dao = self.factory.get_controller('DAOcontroller')
            client_id = self.factory.get_controller('clientController').client_id(client_name)
            work_dao.updateWork(work_id, date_in, date_out, client_id, client_name, vehicle, diagnosis, repair, spare_part_cost, repair_cost, total_price, payment_method, done)
        except WorksExceptions.WorkNotExistException as e:
            raise WorksExceptions.WorkNotExistException("El trabajo no existe")
        
    def work_id(self, client_name):
        work_dao = self.factory.get_controller('DAOcontroller')
        return work_dao.work_id(client_name)
    
    def delete_work(self, work_id):
        try:
            work_dao = self.factory.get_controller('DAOcontroller')
            work_dao.deleteWork(work_id)
        except WorksExceptions.WorkNotExistException as e:
            raise WorksExceptions.WorkNotExistException("El trabajo no existe")
        
    def delete_all_works(self, client_id):
        work_dao = self.factory.get_controller('DAOcontroller')
        work_dao.delete_all_works(client_id)
        
    def list_works_per_month(self, month, year):
            work_dao = self.factory.get_controller('DAOcontroller')
            return work_dao.list_works_per_month(month, year)