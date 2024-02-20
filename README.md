Automotive Workshop Management Software
Introduction
Welcome to our Automotive Workshop Management Software. This tool is designed to streamline the operations of automotive workshops by managing users, tasks performed, and monthly income efficiently. Our software aims to simplify your workshop's administrative tasks, allowing you to focus on providing top-quality services to your clients.

Installation Instructions
Prerequisites
Python: Ensure Python is installed on your system. This software has been tested with Python 3.
PostgreSQL: You will need PostgreSQL installed with the following configurations:
Password: 1234
Port: 5432
Steps
Install Python Requirements: Navigate to the root directory of this project in your terminal or command prompt. Run the following command to install the necessary Python libraries specified in requirements.txt:

pip install -r requirements.txt
Install PostgreSQL: If you haven't already, download and install PostgreSQL. During the installation, set the password to 1234 and the port to 5432 to match the software's default database configuration.

Important: To ensure that your system can interact with PostgreSQL from the command line, you must add the path to PostgreSQL's bin directory to your system's PATH environment variable. This directory is typically found within your PostgreSQL installation path (e.g., C:/Program Files/PostgreSQL/<version>/bin on Windows or /usr/local/pgsql/bin on Unix systems). You can modify the PATH variable through your system's environment settings. Adding PostgreSQL to the PATH makes it possible to execute PostgreSQL commands from any terminal window.

Execute PyInstaller: To build the application, run the following command in your terminal or command prompt:

pyinstaller dualD.spec
This will generate an executable version of the software in the dist directory.

Enjoy the Software: Once the installation is complete, navigate to the dist folder, find the executable, and run it to start managing your automotive workshop more efficiently.

Support
For any issues or questions, please refer to the documentation or contact our support team.

Software de Gestión para Talleres Automotrices
Introducción
Bienvenidos al Software de Gestión para Talleres Automotrices. Esta herramienta está diseñada para optimizar las operaciones de talleres automotrices gestionando usuarios, las tareas realizadas y los ingresos mensuales de manera eficiente. Nuestro software busca simplificar las tareas administrativas de su taller, permitiéndole concentrarse en ofrecer servicios de alta calidad a sus clientes.

Instrucciones de Instalación
Prerrequisitos
Python: Asegúrese de que Python esté instalado en su sistema. Este software ha sido probado con Python 3.x.
PostgreSQL: Necesitará tener instalado PostgreSQL con las siguientes configuraciones:
Contraseña: 1234
Puerto: 5432
Pasos
Instalar Requerimientos de Python: Navegue al directorio raíz de este proyecto en su terminal o línea de comandos. Ejecute el siguiente comando para instalar las librerías de Python necesarias especificadas en requirements.txt:

pip install -r requirements.txt
Instalar PostgreSQL: Si aún no lo ha hecho, descargue e instale PostgreSQL. Durante la instalación, establezca la contraseña en 1234 y el puerto en 5432 para coincidir con la configuración predeterminada de la base de datos del software.

Importante: Para asegurar que su sistema pueda interactuar con PostgreSQL desde la línea de comandos, debe agregar la ruta hacia el directorio bin de PostgreSQL a la variable de entorno PATH de su sistema. Este directorio se encuentra típicamente dentro de la ruta de instalación de PostgreSQL (por ejemplo, C:/Program Files/PostgreSQL/<versión>/bin en Windows o /usr/local/pgsql/bin en sistemas Unix). Puede modificar la variable PATH a través de la configuración de entorno de su sistema. Agregar PostgreSQL al PATH permite ejecutar comandos de PostgreSQL desde cualquier ventana de terminal.

Ejecutar PyInstaller: Para construir la aplicación, ejecute el siguiente comando en su terminal o línea de comandos:

pyinstaller dualD.spec
Esto generará una versión ejecutable del software en el directorio dist.

Disfrutar del Software: Una vez completada la instalación, navegue a la carpeta dist, encuentre el ejecutable y ejecútelo para comenzar a gestionar su taller automotriz de manera más eficiente.

Soporte
Para cualquier problema o pregunta, por favor consulte la documentación o contacte a nuestro equipo de soporte.
