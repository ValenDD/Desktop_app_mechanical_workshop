import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def create_database_if_not_exists(dbname, user, password, host, port):
    try:
        # Connect to the default PostgreSQL database
        conn = psycopg2.connect(
            dbname="postgres",  # Connect to the default database
            user=user,
            password=password,
            host=host,
            port=port
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()

        # Check if the target database already exists
        cur.execute(
            sql.SQL("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s"),
            [dbname]
        )
        exists = cur.fetchone()

        # If the database doesn't exist, create it
        if not exists:
            cur.execute(
                sql.SQL("CREATE DATABASE {}").format(sql.Identifier(dbname))
            )
            print(f"Database '{dbname}' created successfully.")
        else:
            print(f"Database '{dbname}' already exists.")

        # Close cursor and connection
        cur.close()
        conn.close()
    except Exception as e:
        print("Error:", e)