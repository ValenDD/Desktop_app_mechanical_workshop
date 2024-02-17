from views.expensesView import paymentWorkUI
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget
from WindowManager.notice import noticeWindow
from WindowManager.error import errorWindow
from datetime import datetime
from utils.Factory import Factory
from PySide6.QtCore import Qt

class newExpenseWindow(QWidget, paymentWorkUI.Ui_Form):
    def __init__(self):
            super().__init__()
            self.setupUi(self)
            self.setWindowIcon(QIcon('./assets/icono-windows.png'))
            self.setWindowTitle("DualD - Nuevo Pago")
            self.factory = Factory()
            self.pushButton_2.clicked.connect(self._add_expense)
            self.pushButton.clicked.connect(self._close_window)
            
    def _add_expense(self):
        work_name = self.lineEdit.text()
        recive_name = self.lineEdit_2.text()
        amount = self.lineEdit_3.text()
        date = datetime.now().strftime('%Y-%m-%d')
        
        if not (amount.isnumeric()):
            self.error = errorWindow()
            self.error.ErrorLabel.setText("El monto debe ser un número entero")
            self.error.show()
            return
    
        if not (work_name and recive_name and amount):
            self.error = errorWindow()
            self.error.ErrorLabel.setText("Todos los campos son requeridos")
            self.error.show()
            return
        
        if (int(amount) <= 0):
            self.error = errorWindow()
            self.error.ErrorLabel.setText("El monto debe ser mayor a 0")
            self.error.show()
            return
        
        if (work_name == recive_name):
            
            return
        
        self.expenses_controller = self.factory.get_controller('expensesController')
        self.expenses_controller.save_expense(work_name, recive_name, amount, date)
        self.error = noticeWindow()
        self.error.ErrorLabel.setText("Gasto ingresado correctamente")
        self.error.show()
        self._close_window()
        
    def _close_window(self):
        self.close()

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            self._add_expense()
        
        if event.key() == Qt.Key_Escape:
            self._close_window()
        super().keyPressEvent(event)