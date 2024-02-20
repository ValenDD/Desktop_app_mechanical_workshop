import subprocess
import os

def do_backup(db_name, db_user, db_password, db_host, db_port):
    documents_dir = os.path.join(os.path.expanduser('~'), 'Documents', 'BackupsPostgreSQL')
    os.makedirs(documents_dir, exist_ok=True)
    
    backup_file = os.path.join(documents_dir, f'backup_{db_name}.sql')
    
    os.environ["PGPASSWORD"] = db_password
    
    command = f'pg_dump -U {db_user} -h {db_host} -p {db_port} -d {db_name} -f "{backup_file}"'
    
    try:
        subprocess.run(command, check=True, shell=True)
        print('Backup realizado con éxito en:', backup_file)
    except subprocess.CalledProcessError as e:
        print(f'Error al realizar el backup: {e}')
    finally:
        del os.environ["PGPASSWORD"]