from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
import database
import Menu

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(842, 470)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color : rgb(85, 85, 127);\n")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(60, 10, 581, 441))
        self.widget.setStyleSheet("background-color: rgb(233, 233, 233);\n")
        self.widget.setObjectName("widget")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 140, 271, 51))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(230, 310, 131, 41))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 0);\nbackground-color: rgb(255, 255, 228);")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 210, 271, 51))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(80, 220, 91, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(233, 233, 233);\n")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(100, 150, 51, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(233, 233, 233);\n")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(200, 30, 181, 61))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(25)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(233, 233, 233);\ncolor: rgb(85, 170, 0);\n")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Login"))
        self.label_2.setText(_translate("Form", "Password"))
        self.label.setText(_translate("Form", "Email"))
        self.label_3.setText(_translate("Form", "LOGIN PAGE !"))

class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()  # Create an instance of the Ui_Form class
        self.ui.setupUi(self)  # Setup the user interface
        self.ui.pushButton.clicked.connect(self.verify_login)  # Connect the button to the verify_login method

        # Establish the database connection
        self.connection = database.connect_to_database('localhost', 'face_smart', 'root', '')
        if self.connection is None:
            QMessageBox.critical(self, 'Database Connection Error', 'Failed to connect to the database.')

    def verify_login(self):
        email = self.ui.lineEdit.text()  # Get the text from the email input
        password = self.ui.lineEdit_2.text()  # Get the text from the password input

        # Call the login function from the database module
        if self.connection and database.login(email, password, self.connection):
            QMessageBox.information(self, 'Login Success', 'Login successful!')
            
            # Close the current login window
            self.close()

            # Open the menu window
            self.menu_window = QtWidgets.QMainWindow()
            self.menu_ui = Menu.Ui_MainWindow()
            self.menu_ui.setupUi(self.menu_window)
            self.menu_window.show()
        else:
            QMessageBox.warning(self, 'Login Failed', 'Email or Password is incorrect.')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginForm()
    window.show()  # Show the main application window
    sys.exit(app.exec_())
