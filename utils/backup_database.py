import subprocess
import os
from WindowManager.notice import noticeWindow
from WindowManager.error import errorWindow

def do_backup(db_name, db_user, db_password, db_host, db_port):
    documents_dir = os.path.join(os.path.expanduser('~'), 'Documents', 'BackupsPostgreSQL')
    os.makedirs(documents_dir, exist_ok=True)
    
    backup_file = os.path.join(documents_dir, f'backup_{db_name}.sql')
    
    os.environ["PGPASSWORD"] = db_password
    
    command = f'pg_dump -U {db_user} -h {db_host} -p {db_port} -d {db_name} -f "{backup_file}"'
    
    try:
        subprocess.run(command, check=True, shell=True)
        error = noticeWindow()
        error.ErrorLabel.setText("Backup realizado con éxito")
        error.show()
    except subprocess.CalledProcessError as e:
        error = errorWindow()
        error.ErrorLabel.setText("Error al realizar el backup")
        error.show()
    finally:
        del os.environ["PGPASSWORD"]