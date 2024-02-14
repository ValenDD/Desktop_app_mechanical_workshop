from views.clientView import BuscarClienteUI
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget
from WindowManager.fiendedClient import findedClientWindow

class findClientWindow(QWidget, BuscarClienteUI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./assets/icono-windows.png'))
        self.setWindowTitle("DualD - Buscar Cliente")

        self.Buscar_Usuarios.clicked.connect(self._show_finded_client)
        
    def _show_finded_client(self):
            Nombre = self.Nombre_line_edit.text()
            Apellido = self.Apellido_line_edit.text()
            NombreCompleto = Nombre + " " + Apellido
            self.finded_users = findedClientWindow(NombreCompleto)
            self.finded_users.show()
            self._close_window()
            
    def _close_window(self):
        self.close()