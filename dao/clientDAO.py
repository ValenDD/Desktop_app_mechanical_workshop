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

    def close_conection(self):
        self.conn.close()