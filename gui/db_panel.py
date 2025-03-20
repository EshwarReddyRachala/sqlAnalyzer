from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox
from database.connection import get_connection

class DBPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.connection = None

        layout = QVBoxLayout(self)

        self.db_type = QComboBox()
        self.db_type.addItems(["SQLite", "PostgreSQL", "MySQL"])
        self.host_input = QLineEdit()
        self.host_input.setPlaceholderText("Host (if applicable)")
        self.db_name_input = QLineEdit()
        self.db_name_input.setPlaceholderText("Database Name")
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText("Username (if applicable)")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password (if applicable)")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.connect_button = QPushButton("Connect")
        self.connect_button.clicked.connect(self.connect_to_database)

        layout.addWidget(QLabel("Database Type:"))
        layout.addWidget(self.db_type)
        layout.addWidget(QLabel("Host:"))
        layout.addWidget(self.host_input)
        layout.addWidget(QLabel("Database Name:"))
        layout.addWidget(self.db_name_input)
        layout.addWidget(QLabel("Username:"))
        layout.addWidget(self.user_input)
        layout.addWidget(QLabel("Password:"))
        layout.addWidget(self.password_input)
        layout.addWidget(self.connect_button)

    def connect_to_database(self):
        db_type = self.db_type.currentText()
        host = self.host_input.text()
        db_name = self.db_name_input.text()
        user = self.user_input.text()
        password = self.password_input.text()

        try:
            self.connection = get_connection(db_type, host, db_name, user, password)
            print(f"Successfully connected to {db_type}")
        except Exception as e:
            print(f"Connection failed: {e}")