from PyQt6.QtWidgets import QWidget, QHBoxLayout, QSplitter
from PyQt6.QtCore import Qt
from .db_panel import DBPanel
from .query_panel import QueryPanel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SQL Analyzer")
        self.setGeometry(100, 100, 1200, 800)

        layout = QHBoxLayout(self)
        splitter = QSplitter(Qt.Orientation.Horizontal)

        self.db_panel = DBPanel()
        self.query_panel = QueryPanel(self.db_panel)

        splitter.addWidget(self.db_panel)
        splitter.addWidget(self.query_panel)
        layout.addWidget(splitter)
