from PyQt5 import QtCore, QtGui, QtWidgets
import database

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(925, 600)
        MainWindow.setStyleSheet("background-color:#fff;")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Main layout
        self.main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setAlignment(QtCore.Qt.AlignCenter)

        # Container widget
        self.container_widget = QtWidgets.QWidget(self.centralwidget)
        self.container_layout = QtWidgets.QVBoxLayout(self.container_widget)
        self.container_layout.setAlignment(QtCore.Qt.AlignCenter)

        self.textBrowser = QtWidgets.QTextBrowser(self.container_widget)
        self.textBrowser.setObjectName("textBrowser")
        self.container_layout.addWidget(self.textBrowser)

        self.form_layout = QtWidgets.QGridLayout()
        self.form_layout.setAlignment(QtCore.Qt.AlignCenter)

        self.label = QtWidgets.QLabel(self.container_widget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
                                  "font-size:14px")
        self.label.setObjectName("label")
        self.form_layout.addWidget(self.label, 0, 0)

        self.lineEdit = QtWidgets.QLineEdit(self.container_widget)
        self.lineEdit.setObjectName("lineEdit")
        self.form_layout.addWidget(self.lineEdit, 0, 1)

        self.label_3 = QtWidgets.QLabel(self.container_widget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
                                  "font-size:14px")
        self.label_3.setObjectName("label_3")
        self.form_layout.addWidget(self.label_3, 0, 2)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.container_widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.form_layout.addWidget(self.lineEdit_2, 0, 3)

        self.label_2 = QtWidgets.QLabel(self.container_widget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
                                  "font-size:14px")
        self.label_2.setObjectName("label_2")
        self.form_layout.addWidget(self.label_2, 1, 0)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.container_widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.form_layout.addWidget(self.lineEdit_3, 1, 1)

        self.label_4 = QtWidgets.QLabel(self.container_widget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);\n"
                                  "font-size:14px")
        self.label_4.setObjectName("label_4")
        self.form_layout.addWidget(self.label_4, 1, 2)

        self.lineEdit_4 = QtWidgets.QLineEdit(self.container_widget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)  # Set as password field
        self.form_layout.addWidget(self.lineEdit_4, 1, 3)

        self.label_5 = QtWidgets.QLabel(self.container_widget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);\n"
                                  "font-size:14px")
        self.label_5.setObjectName("label_5")
        self.form_layout.addWidget(self.label_5, 2, 0)

        self.lineEdit_5 = QtWidgets.QLineEdit(self.container_widget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.form_layout.addWidget(self.lineEdit_5, 2, 1)

        self.label_6 = QtWidgets.QLabel(self.container_widget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);\n"
                                  "font-size:14px")
        self.label_6.setObjectName("label_6")
        self.form_layout.addWidget(self.label_6, 2, 2)

        self.pushButton_5 = QtWidgets.QPushButton(self.container_widget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.form_layout.addWidget(self.pushButton_5, 2, 3)

        self.container_layout.addLayout(self.form_layout)

        self.pushButton_6 = QtWidgets.QPushButton(self.container_widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "border:none;\n"
                                        "background-color: rgb(0, 0, 0);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.container_layout.addWidget(self.pushButton_6)

        self.main_layout.addWidget(self.container_widget, 0, QtCore.Qt.AlignCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 925, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "hr { height: 1px; border-width: 0; }\n"
                                            "li.unchecked::marker { content: \"\\2610\"; }\n"
                                            "li.checked::marker { content: \"\\2612\"; }\n"
                                            "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:700;\">Ajouter Employée</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "Nom"))
        self.label_2.setText(_translate("MainWindow", "Email"))
        self.label_3.setText(_translate("MainWindow", "Prenom"))
        self.label_4.setText(_translate("MainWindow", "Password"))
        self.label_5.setText(_translate("MainWindow", "Departement"))
        self.pushButton_5.setText(_translate("MainWindow", "parcourir"))
        self.label_6.setText(_translate("MainWindow", "Image"))
        self.pushButton_6.setText(_translate("MainWindow", "Ajouter"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton_6.clicked.connect(self.ajouter_employe)
        self.pushButton_5.clicked.connect(self.browse_file)

    def browse_file(self):
        self.file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Choisir une image", "",
                                                                   "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if self.file_path:
            # Set the file path to some variable or display it somewhere
            print("Selected File:", self.file_path)

    def ajouter_employe(self):
        # Retrieve other employee information as before
        nom = self.lineEdit.text()
        prenom = self.lineEdit_3.text()
        email = self.lineEdit_2.text()
        password = self.lineEdit_4.text()
        departement = self.lineEdit_5.text()

        # Read the image file as binary data
        with open(self.file_path, 'rb') as f:
            image_data = f.read()
        
        database.insert_employee(nom, prenom, email, password, departement, image_data)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
