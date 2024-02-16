import psycopg2

class ExpensesDAO:
    def __init__(self, db_config):
        self.conn = psycopg2.connect(**db_config)
    
    def close_conection(self):
        self.conn.close()
        
    def save(self, work_name, recive_name, amount, date):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO ganancias (nombre_trabajo, nombre_receptor, fecha_ingreso, monto) VALUES (%s, %s, %s, %s)", (work_name, recive_name, date, amount))
        self.conn.commit()
        cursor.close()
        
    def list_expenses(self, month, year):
        cursor = self.conn.cursor()
        cursor.execute("SELECT nombre_trabajo, nombre_receptor, fecha_ingreso, monto FROM ganancias WHERE EXTRACT(MONTH FROM fecha_ingreso) = %s AND EXTRACT(YEAR FROM fecha_ingreso) = %s", (month, year))
        expenses = cursor.fetchall()
        cursor.close()
        return expenses
    
    def expense_id(self, work_name, recive_name, amount):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id_ganancia FROM ganancias WHERE nombre_trabajo = %s AND nombre_receptor = %s AND monto = %s", (work_name, recive_name, amount))
        expense = cursor.fetchone()
        cursor.close()
        return expense
    
    def update(self, id_expense, work_name, recive_name, amount):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE ganancias SET nombre_trabajo = %s, nombre_receptor = %s, monto = %s WHERE id_ganancia = %s", (work_name, recive_name, amount, id_expense))
        self.conn.commit()
        cursor.close()