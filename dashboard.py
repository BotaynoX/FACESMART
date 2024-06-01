from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from mysql.connector import Error
import database  # Assurez-vous que database.py est importé correctement
import datetime

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(925, 600)
        MainWindow.setStyleSheet("background-color:#fff;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.navbar = QtWidgets.QGraphicsView(self.centralwidget)
        self.navbar.setGeometry(QtCore.QRect(0, 0, 161, 591))
        self.navbar.setStyleSheet("border:none")
        self.navbar.setObjectName("navbar")

        # Centering the "Employees" button
        button_width = 201
        button_height = 41
        main_window_width = 925
        x_coordinate = (main_window_width - button_width) // 2
        y_coordinate = 470
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(x_coordinate, y_coordinate, button_width, button_height))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(False)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("border:none;\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "\n"
                                      "background-color: #000000;\n"
                                      "border-radius:20%;\n"
                                      "font-size:15px;")
        self.pushButton.setObjectName("pushButton")

        # Adding input field under the "Employees" button
        input_width = 201
        input_height = 30
        input_y_coordinate = y_coordinate + button_height + 10  # 10 pixels below the button
        self.deleteInput = QtWidgets.QLineEdit(self.centralwidget)
        self.deleteInput.setGeometry(QtCore.QRect(x_coordinate, input_y_coordinate, input_width, input_height))
        self.deleteInput.setObjectName("deleteInput")
        self.deleteInput.setPlaceholderText("Id to Delete")
        self.deleteInput.setStyleSheet("font-size:15px; padding: 5px;")

        # Adding "Delete Employee" button under the input field
        delete_button_width = 201
        delete_button_height = 41
        delete_button_y_coordinate = input_y_coordinate + input_height + 10  # 10 pixels below the input field
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(x_coordinate, delete_button_y_coordinate, delete_button_width, delete_button_height))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.deleteButton.setFont(font)
        self.deleteButton.setMouseTracking(False)
        self.deleteButton.setAutoFillBackground(False)
        self.deleteButton.setStyleSheet("border:none;\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "\n"
                                        "background-color: #FF0000;\n"
                                        "border-radius:20%;\n"
                                        "font-size:15px;")
        self.deleteButton.setObjectName("deleteButton")

        # Table Widget
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(280, 100, 491, 341))
        self.tableWidget.setStyleSheet("\n")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)  # Update the column count to 8
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)  # New column for Password
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)  # New column for Worked Hours

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
        self.pushButton.clicked.connect(self.load_employees)
        self.deleteButton.clicked.connect(self.delete_employee)
        # Connect button clicks to functions
        self.pushButton.clicked.connect(self.load_employees)
        self.deleteButton.clicked.connect(self.delete_employee)
        self.deleteButton.clicked.connect(self.print_employee_id)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Employees"))
        self.deleteInput.setPlaceholderText(_translate("MainWindow", "Id to Delete"))
        self.deleteButton.setText(_translate("MainWindow", "Delete Employee"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nom"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Prenom"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Email"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Password"))  # Updated column header for Password
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Dep"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Etats"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Worked Hours"))  # New column header for Worked Hours

    def load_employees(self):
        connection = database.connect_to_database(
            host='localhost',
            database='face_smart',
            user='root',
            password=''
        )
        if connection is None:
            print("Failed to connect to the database.")
            return

        employees = database.AfficheDa(connection)
        if employees is False:
            print("Failed to retrieve data.")
            return

        self.tableWidget.setRowCount(len(employees))
        for row, employee in enumerate(employees):
            for col, value in enumerate(employee):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.tableWidget.setItem(row, col, item)

            # Call checkStatus function for the current employee ID
            employee_id = employee[0]  # Assuming the ID is the first column
            status = database.checkStatus(employee_id)
            
            # Add status to the last column
            status_item = QtWidgets.QTableWidgetItem(status)
            self.tableWidget.setItem(row, len(employee), status_item)

            today_date = datetime.datetime.now().strftime("%Y-%m-%d")

            # Call calculate_work_time function for the current employee ID to retrieve worked hours
            worked_hours = database.calculate_work_time(connection, employee_id, today_date)

            # Add worked hours to the new column as a message
            worked_hours_message = f"{worked_hours}"
            worked_hours_item = QtWidgets.QTableWidgetItem(worked_hours_message)
            self.tableWidget.setItem(row, len(employee) + 1, worked_hours_item)

        connection.close()
        
    def print_employee_id(self):
        employee_id = self.deleteInput.text()
        # print("ID to delete:", employee_id)
        database.delete_employee(employee_id)

    def delete_employee(self):
        employee_id = self.deleteInput.text()
        if not employee_id:
            print("Please enter an employee ID.")
            return

        connection = database.connect_to_database(
            host='localhost',
            database='face_smart',
            user='root',
            password=''
        )
        if connection is None:
            print("Failed to connect to the database.")
            return

        result = database.delete_employee( employee_id)
        connection.close()

        if result:
            print(f"Employee with ID {employee_id} has been deleted.")
            self.load_employees()
        else:
            print("Failed to delete employee.")

# Main application code to run the UI
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
