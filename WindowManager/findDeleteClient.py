from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon
from utils.Factory import Factory
from views.clientView import findDeleteClientWindowUI
from utils.Factory import Factory
from WindowManager.error import errorWindow
from exceptions import exceptions


class findDeleteClientWindow(QWidget, findDeleteClientWindowUI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./assets/icono-windows.png'))
        self.setWindowTitle("DualD - Buscar Cliente")
        
        self.factory = Factory()
        self.client_controller = self.factory.get_controller("clientController")
        clients = self.client_controller.list_client_only_name()
        for index in range(len(clients)):
            self.lista_clientes.addItem(clients[index][0])
        
        self.Eliminar_cliente.clicked.connect(self._delete_client)
        
    def _delete_client(self):
        client_name = self.lista_clientes.currentText()
        try:
            self.client_controller.delete_client(client_name)
            self.error = errorWindow()
            self.error.ErrorLabel.setText("Cliente eliminado con éxito")
            self.error.show()
            self.close()
        except exceptions.ClientNotExistException as e:
            self.error = errorWindow()
            self.error.ErrorLabel.setText(str(e))
            self.error.show()
        except Exception as e:
            self.error = errorWindow()
            self.error.ErrorLabel.setText(str(e))
            self.error.show()
        