from dao.clientDAO import ClientDAO
from dao.workDAO import WorkDAO
from dao.expensesDAO import ExpensesDAO
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
    
    def client_id(self, name):
        client_dao = ClientDAO(self.set_dbconfig())
        client = client_dao.client_id(name)
        client_dao.close_conection()
        return client
    
    def deleteClient(self, name):
        client_dao = ClientDAO(self.set_dbconfig())
        client_dao.delete(name)
        client_dao.close_conection()
        
#WorkDAO
    def saveWork(self, client_it, work):
        work_dao = WorkDAO(self.set_dbconfig())
        work_dao.save(client_it, work)
        work_dao.close_conection()

    def listWorks(self):
        work_dao = WorkDAO(self.set_dbconfig())
        works = work_dao.list()
        work_dao.close_conection()
        return works
    
    def searchClientWorks(self, client_name):
        work_dao = WorkDAO(self.set_dbconfig())
        works = work_dao.search_works(client_name)
        work_dao.close_conection()
        return works
    
    def updateWork(self, work_id, date_in, date_out, client_id, client_name, vehicle, diagnosis, repair, spare_part_cost, repair_cost, total_price, payment_method, done):
        work_dao = WorkDAO(self.set_dbconfig())
        work_dao.update(work_id, date_in, date_out, client_id, client_name, vehicle, diagnosis, repair, spare_part_cost, repair_cost, total_price, payment_method, done)
        work_dao.close_conection()
        
    def work_id(self, client_name):
        work_dao = WorkDAO(self.set_dbconfig())
        work = work_dao.work_id(client_name)
        work_dao.close_conection()
        return work
    
    def deleteWork(self, work_id):
        work_dao = WorkDAO(self.set_dbconfig())
        work_dao.delete(work_id)
        work_dao.close_conection()
        
    def delete_all_works(self, client_id):
        work_dao = WorkDAO(self.set_dbconfig())
        work_dao.delete_all_works(client_id)
        work_dao.close_conection()
    
    def list_works_per_month(self, month, year):
            work_dao = WorkDAO(self.set_dbconfig())
            works = work_dao.list_works_per_month(month, year)
            work_dao.close_conection()
            return works
        
    #ExpensesDAO
    def save_expense(self, work_name, recive_name, amount, date):
        expenses_dao = ExpensesDAO(self.set_dbconfig())
        expenses_dao.save(work_name, recive_name, amount, date)
        expenses_dao.close_conection()
        
    def list_expenses(self, month, year):
        expenses_dao = ExpensesDAO(self.set_dbconfig())
        expenses = expenses_dao.list_expenses(month, year)
        expenses_dao.close_conection()
        return expenses
    
    def expense_id(self, work_name, recive_name, amount):
        expenses_dao = ExpensesDAO(self.set_dbconfig())
        expense = expenses_dao.expense_id(work_name, recive_name, amount)
        expenses_dao.close_conection()
        return expense
    
    def update_expense(self, id_expense, work_name, recive_name, amount):
        expenses_dao = ExpensesDAO(self.set_dbconfig())
        expenses_dao.update(id_expense, work_name, recive_name, amount)
        expenses_dao.close_conection()