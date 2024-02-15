import psycopg2

class WorkDAO:
    def __init__(self, db_config):
        self.conn = psycopg2.connect(**db_config)
    
    def save(self, work):
        with self.conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO trabajos (Fecha_ingreso, Fecha_egreso, Nombre_cliente, Vehiculo, Diagnostico, Reparacion, Costo_repuestos, Costo_reparacion, Precio_total, Metodo_de_pago, Terminado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (work._date_in, work._date_out, work._client_name, work._vehicle, work._diagnosis, work._repair, work._spare_part_cost, work._repair_cost, work._total_price, work._payment_method, work._done)
            )
            self.conn.commit()
    
    def close_conection(self):
        self.conn.close()