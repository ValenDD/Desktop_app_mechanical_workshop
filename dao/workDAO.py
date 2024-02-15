import psycopg2

class WorkDAO:
    def __init__(self, db_config):
        self.conn = psycopg2.connect(**db_config)
    
    def save(self, client_id, work):
        with self.conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO trabajos (client_id, Fecha_ingreso, Fecha_egreso, Nombre_cliente, Vehiculo, Diagnostico, Reparacion, Costo_repuestos, Costo_reparacion, Precio_total, Metodo_de_pago, Terminado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (client_id, work._date_in, work._date_out, work._client_name, work._vehicle, work._diagnosis, work._repair, work._spare_part_cost, work._repair_cost, work._total_price, work._payment_method, work._done)
            )
            self.conn.commit()
    
    def list(self):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM trabajos")
            return cursor.fetchall()
    
    def search_works(self, client_name):
        with self.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM trabajos WHERE Nombre_cliente = %s", (client_name,))
            return cursor.fetchall()
    
    def close_conection(self):
        self.conn.close()