from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget
from PySide6.QtSql import QSqlDatabase, QSqlQuery


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 600)

        # Create a database connection
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("./database.db")
        if not db.open():
            print("Error opening database:", db.lastError().text())

        # Create a table widget
        self.table_widget = QTableWidget(self)
        # Adjust the number of columns as needed
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(
            ["ID", "username", "password"])

        # Create a button to trigger data display
        self.show_data_button = QPushButton("Show Data", self)
        self.insert = QPushButton("Insert", self)

        self.show_data_button.clicked.connect(self.show_data)
        self.insert.clicked.connect(self.insert_data)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        layout.addWidget(self.show_data_button)
        layout.addWidget(self.insert)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def insert_data(self):
        self.table_widget.clearContents()

    def show_data(self):
        # Clear existing data from the table widget
        self.table_widget.clearContents()

        # Fetch data from the "Persons" table
        query = QSqlQuery("SELECT * FROM users")
        row = 0
        while query.next():
            id = query.value(0)  # Assuming column 1 contains names
            username = query.value(1)   # Assuming column 2 contains ages
            password = query.value(2)

            # Add more lines for additional columns as needed

            # Insert data into the table widget
            self.table_widget.insertRow(row)
            item_id = QTableWidgetItem(str(id))
            item_username = QTableWidgetItem(username)
            item_password = QTableWidgetItem(password)

            # Add more lines for additional columns as needed
            self.table_widget.setItem(row, 0, item_id)
            self.table_widget.setItem(row, 1, item_username)
            self.table_widget.setItem(row, 2, item_password)

            # Add more lines for additional columns as needed
            row += 1


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
