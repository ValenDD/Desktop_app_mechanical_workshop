# 🚗 **Automotive Workshop Management Software** 🔧

---

## 🛠️ **Introduction**

Welcome to our **Automotive Workshop Management Software**. This tool is designed to streamline the operations of automotive workshops by managing users, tasks performed, and monthly income efficiently. Our software aims to simplify your workshop's administrative tasks, allowing you to focus on providing top-quality services to your clients.

---

## 📥 **Installation Instructions**

### ⚙️ **Prerequisites**

- **🐍 Python**: Ensure Python is installed on your system. This software has been tested with Python 3.x.
- **🐘 PostgreSQL**: You will need PostgreSQL installed with the following configurations:
  - **Password**: `1234`
  - **Port**: `5432`

### 📋 **Steps**

1. **📦 Install Python Requirements**: Navigate to the root directory of this project in your terminal or command prompt. Run the following command to install the necessary Python libraries specified in `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

2. **🐘 Install PostgreSQL**: If you haven't already, download and install PostgreSQL. During the installation, set the password to `1234` and the port to `5432` to match the software's default database configuration.

    > **Important**: To ensure that your system can interact with PostgreSQL from the command line, you must add the path to PostgreSQL's `bin` directory to your system's PATH environment variable. This directory is typically found within your PostgreSQL installation path (e.g., `C:/Program Files/PostgreSQL/<version>/bin` on Windows or `/usr/local/pgsql/bin` on Unix systems). You can modify the PATH variable through your system's environment settings. Adding PostgreSQL to the PATH makes it possible to execute PostgreSQL commands from any terminal window.

3. **🛠️ Execute PyInstaller**: To build the application, run the following command in your terminal or command prompt:

    ```bash
    pyinstaller dualD.spec
    ```

    This will generate an executable version of the software in the `dist` directory.

4. **🚀 Enjoy the Software**: Once the installation is complete, navigate to the `dist` folder, find the executable, and run it to start managing your automotive workshop more efficiently.

---

