from PyQt5 import QtCore, QtGui, QtWidgets
import database  # Make sure database.py is imported correctly
import datetime
import dashboard  # Import the dashboard module
import Ajouter  # Import the Ajouter module

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow  # Store reference to MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(925, 600)
        MainWindow.setStyleSheet("background-color:#fff;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(False)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("border:none;\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: #000000;\n"
                                      "border-radius:20%;\n"
                                      "font-size:15px;")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setStyleSheet("border:none;\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "background-color:#000000;\n"
                                        "border-radius:20%;\n"
                                        "font-size:15px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 925, 17))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect button clicks to functions
        self.pushButton.clicked.connect(self.load_dashboard)
        self.pushButton_2.clicked.connect(self.add_employee)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "DASHBOARD"))
        self.pushButton_2.setText(_translate("MainWindow", "ADD EMPLOYEE"))

    def load_dashboard(self):
        self.MainWindow.close()  # Close the current main window
        self.window = QtWidgets.QMainWindow()
        self.ui = dashboard.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def add_employee(self):
        self.MainWindow.close()  # Close the current main window
        self.window = QtWidgets.QMainWindow()
        self.ui = Ajouter.Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

# Main application code to run the UI
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
