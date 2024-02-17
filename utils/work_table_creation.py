import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from dotenv import load_dotenv
import os

def create_tables_if_not_exist(db_name, db_user, db_password, db_host, db_port):
    try:
        # Connect to the server
        load_dotenv()
        conn = psycopg2.connect(dbname=db_name, user=db_user, password=db_password, host=db_host, port=db_port)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()

        # Check if the table exists
        query = sql.SQL("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_schema = 'public' AND table_name = %s)")
        cur.execute(query, ['trabajos'])        
        exists = cur.fetchone()[0]

        # if not, create the table
        if not exists:
            cur.execute(
                """
                CREATE TABLE trabajos (
                    id_trabajo SERIAL PRIMARY KEY,
                    client_id INT,
                    Fecha_ingreso DATE,
                    Fecha_egreso DATE,
                    Nombre_cliente VARCHAR(255),
                    Vehiculo VARCHAR(255),
                    Diagnostico TEXT,
                    Reparacion TEXT,
                    Costo_repuestos DECIMAL(10, 2),
                    Costo_reparacion DECIMAL(10, 2),
                    Precio_total DECIMAL(10, 2),
                    Metodo_de_pago TEXT,
                    Terminado BOOLEAN,
                    FOREIGN KEY (client_id) REFERENCES clientes(id)
                )
                """
            )
            print("Tabla 'trabajos' creada exitosamente.")
        else:
            print("La tabla 'trabajos' ya existe.")

        # Close the cursor and the connection
        cur.close()
        conn.close()
    except Exception as e:
        print("Error:", e)