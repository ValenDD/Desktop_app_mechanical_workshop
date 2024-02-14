from PySide6.QtWidgets import QWidget
from views.clientView import updateClientUI
from PySide6.QtGui import QIcon
from WindowManager.error import errorWindow
from exceptions import exceptions
from utils.Factory import Factory

class updateSearchClient(QWidget, updateClientUI.Ui_Form):
    def __init__(self, clients):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./assets/icono-windows.png'))
        self.setWindowTitle("DualD - Clientes Encontrados")
        self.clients = clients

        self.pushButton.clicked.connect(self._close_window)
        self.label_2.setVisible(False)
        self.label_3.setVisible(False)
        self.lineEdit.setVisible(False)
        self.lineEdit_2.setVisible(False)
        self.pushButton_2.setVisible(False)
        self.pushButton.setVisible(False)
        
        self.comboBox.addItem("")
        for index in range(len(clients)):
            self.comboBox.addItem(clients[index][0])
            
        self.comboBox.currentIndexChanged.connect(self.on_comboBox_changed)
        self.lineEdit.textChanged.connect(self.on_lineEdit_changed)
        self.lineEdit_2.textChanged.connect(self.on_lineEdit_changed)
        self.on_comboBox_changed(self.comboBox.currentIndex())
        self.pushButton_2.clicked.connect(self.update_client)
        self.pushButton.clicked.connect(self._close_window)
        
    def _close_window(self):
        self.close()
        
    def on_comboBox_changed(self, index):
        if index > 0:
            self.label_2.setVisible(True)
            self.label_3.setVisible(True)
            self.lineEdit.setVisible(True)
            self.lineEdit_2.setVisible(True)
            self.pushButton_2.setVisible(True)
            self.pushButton.setVisible(True)
            self.factory = Factory()
            self.client_controller = self.factory.get_controller('clientController')
            client = self.client_controller.find_users(self.comboBox.currentText())
            self.lineEdit.setText(client[0][1])
            self.lineEdit_2.setText(client[0][2])
        else:
            self.label_2.setVisible(False)
            self.label_3.setVisible(False)
            self.lineEdit.setVisible(False)
            self.lineEdit_2.setVisible(False)
            
    def on_lineEdit_changed(self, ):
        self.factory = Factory()
        self.client_controller = self.factory.get_controller('clientController')
        client = self.client_controller.find_users(self.comboBox.currentText())
        name_changed = False
        phone_changed = False
        
        if self.lineEdit.text() != client[0][1]:
            name_changed = True
        if self.lineEdit_2.text() != client[0][2]:
            phone_changed = True
        if name_changed or phone_changed:
            self.pushButton_2.setEnabled(True)
        
    def update_client(self):
        if len(self.lineEdit_2.text().strip()) < 9:
            self.error = errorWindow()
            self.error.ErrorLabel.setText("El teléfono debe ser menor a 8 digitos")
            self.error.show()
            return
        
        try:
            self.client_controller.update_client_name(self.comboBox.currentText(), self.lineEdit.text().strip(), self.lineEdit_2.text().strip())
            self.error = errorWindow()
            self.error.ErrorLabel.setText("Cliente actualizado correctamente")
            self.error.show()
        except exceptions.ClientNotExistException as e:
            self.error = errorWindow()
            self.error.ErrorLabel.setText(str(e))
            self.error.show()
        except Exception as e:
            self.error = errorWindow()
            self.error.ErrorLabel.setText(str(e))
            self.error.show()