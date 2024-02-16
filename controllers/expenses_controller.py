from models import expenses

class ExpensesController:
    _instance = None
    _factory = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ExpensesController, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        from utils.Factory import Factory
        if not hasattr(self, 'is_initialized'):
            self.is_initialized = True
        self.factory = Factory()

    def save_expense(self, work_name, recive_name, amount, date):
        self.factory.get_controller('DAOcontroller').save_expense(work_name, recive_name, amount, date)

    def list_expenes(self, month, year):
        return self.factory.get_controller('DAOcontroller').list_expenses(month, year)
    
    def calcualte_gains(self, month, year):
        expenses = self.list_expenes(month, year)
        total = 0
        for expense in expenses:
            total += expense[3]
        return total
    
    def expense_id(self, work_name, recive_name, amount):
        return self.factory.get_controller('DAOcontroller').expense_id(work_name, recive_name, amount)
    
    def update_expense(self, id_expense, work_name, recive_name, amount):
        self.factory.get_controller('DAOcontroller').update_expense(id_expense, work_name, recive_name, amount)