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

    def client_exists(self, phone):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM clientes WHERE telefono = %s", (phone,))
            return cursor.fetchone()

    def close_conection(self):
        self.conn.close()