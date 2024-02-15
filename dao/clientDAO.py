import psycopg2

class ClientDAO:
    def __init__(self, db_config):
        self.conn = psycopg2.connect(**db_config)

    def save(self, client):
        with self.conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO clientes (nombre, telefono) VALUES (%s, %s)",
                (client._name, client._phone)
            )
            self.conn.commit()

    def list(self):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM clientes")
            return cursor.fetchall()

    def list_only_name(self):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT nombre FROM clientes")
            return cursor.fetchall()

    def client_exists(self, name):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM clientes WHERE nombre = %s", (name,))
            return cursor.fetchone()

    def close_conection(self):
        self.conn.close()

    def find(self, name):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM clientes WHERE nombre = %s", (name,))
            return cursor.fetchall()
        
    def update(self, name, new_name, new_phone):
        with self.conn.cursor() as cursor:
            cursor.execute(
                "UPDATE clientes SET nombre = %s, telefono = %s WHERE nombre = %s",
                (new_name, new_phone, name)
            )
            self.conn.commit() 
    
    def client_id(self, name):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT id FROM clientes WHERE nombre = %s", (name,))
            return cursor.fetchone()
    
    def delete(self, name):
        with self.conn.cursor() as cursor:
            cursor.execute("DELETE FROM clientes WHERE nombre = %s", (name,))
            self.conn.commit()