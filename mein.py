from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtWidgets import QApplication
from password import Ui_MainWinow

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWinow()
        self.ui.setpUi(self)
        self.ui.btn_OK.clicked.connect(self.generate)

    def generate(self):
        s_number = '0123456789'
        s_alphabet = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
        pas = ''
        if self.ui.cb_number.isChecked():
            for i in range(16):
                pas = pas + random.choise(s_number)
        if self.ui.cb_alphabet.isChecked():
            for i in range(16):
                pas = pas + random.choise(s_number + s_alphabet)
        self.ui.resulut.setText(pas)
        

app = QApplication([])
window = Widget()




window.show()
app.exec_()