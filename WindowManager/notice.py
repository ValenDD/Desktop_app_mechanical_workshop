from PySide6.QtWidgets import QWidget
from views.NoticeView import avisoUI
from PySide6.QtGui import QIcon


class noticeWindow(QWidget, avisoUI.Ui_Frame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./assets/icono-windows.png'))
        self.setWindowTitle("Aviso")
        
    