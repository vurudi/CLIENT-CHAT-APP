from PyQt5.QtWidgets import *
from PyQt5 import uic


class LoginUi(QMainWindow):
    def __init__(self):
        super(LoginUi, self).__init__()
        uic.loadUi("FTV100CLIENTLOGIN.ui", self)
        self.show()
        self.btnlogin.clicked.connect(self.login)
        self.btnforgotpassword.clicked.connect(self.getpassword)
        self.btnregister.clicked.connect(self.registerwindow)

    def login(self):
        with open('logemail.txt', 'r') as f:
            u_email = f.read('ascii')
        with open('logpassword.txt', 'r') as f:
            u_pass = f.read('ascii')
        if self.txtloginpass.text() == u_email and self.txtloginpass.text() == u_pass:
            self.txtloginemail.setText('')
        else:
            pass

    def getpassword(self):
        pass

    def registerwindow(self):
        pass

    def ui_main(self):
        app = QApplication([])
        window = LoginUi()
        app.exec_()


class RegisterUi(QMainWindow):
    def __init__(self):
        super(RegisterUi, self).__init__()
        uic.loadUi("FTV100CLIENTREG.ui", self)
        self.show()

    def Reg_ui_main(self):
        app = QApplication([])
        window = LoginUi()
        app.exec_()


class ChatWindow(QMainWindow):
    def __init__(self):
        super(ChatWindow, self).__init__()
        uic.loadUi("FTV100CLIENT.ui", self)
        self.show()

    def cw_ui_main(self):
        app = QApplication([])
        window = LoginUi()
        app.exec_()


if __name__ == '__main__':
    LoginUi.ui_main('me')
