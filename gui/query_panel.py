from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QListWidget, QFileDialog
from PyQt6.Qsci import QsciScintilla, QsciLexerSQL
from query.executor import execute_query
from query.history import QueryHistory
from query.exporter import export_to_csv
from ai.sql_corrector import correct_query

class QueryPanel(QWidget):
    def __init__(self, db_panel):
        super().__init__()
        self.db_panel = db_panel
        self.history = QueryHistory()

        layout = QVBoxLayout(self)

        self.sql_editor = QsciScintilla()
        lexer = QsciLexerSQL()
        self.sql_editor.setLexer(lexer)
        self.sql_editor.setAutoCompletionThreshold(2)
        self.sql_editor.setAutoCompletionSource(QsciScintilla.AutoCompletionSource.AcsAll)

        self.run_query_button = QPushButton("Run Query")
        self.run_query_button.clicked.connect(self.run_query)
        self.correct_query_button = QPushButton("AI Correct SQL")
        self.correct_query_button.clicked.connect(self.ai_correct_sql)
        self.result_table = QTableWidget()

        self.export_button = QPushButton("Export to CSV")
        self.export_button.clicked.connect(self.export_results)

        self.query_history = QListWidget()
        self.query_history.itemClicked.connect(self.load_query_from_history)

        layout.addWidget(QLabel("SQL Editor:"))
        layout.addWidget(self.sql_editor)
        layout.addWidget(self.run_query_button)
        layout.addWidget(self.correct_query_button)
        layout.addWidget(QLabel("Query History:"))
        layout.addWidget(self.query_history)
        layout.addWidget(QLabel("Query Results:"))
        layout.addWidget(self.result_table)
        layout.addWidget(self.export_button)

    def run_query(self):
        connection = self.db_panel.connection
        if not connection:
            print("No database connected")
            return

        query = self.sql_editor.text()
        try:
            results, columns = execute_query(connection, query)
            self.display_results(results, columns)
            self.history.add_query(query)
            self.query_history.addItem(query)
        except Exception as e:
            print(f"Query failed: {e}")

    def display_results(self, results, columns):
        self.result_table.setColumnCount(len(columns))
        self.result_table.setHorizontalHeaderLabels(columns)
        self.result_table.setRowCount(len(results))

        for row_idx, row_data in enumerate(results):
            for col_idx, col_data in enumerate(row_data):
                self.result_table.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

    def ai_correct_sql(self):
        original_query = self.sql_editor.text()
        corrected_query = correct_query(original_query)
        self.sql_editor.setText(corrected_query)

    def export_results(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save CSV", "", "CSV Files (*.csv)")
        if filename:
            columns = [self.result_table.horizontalHeaderItem(i).text() for i in range(self.result_table.columnCount())]
            data = []
            for row in range(self.result_table.rowCount()):
                row_data = []
                for col in range(self.result_table.columnCount()):
                    item = self.result_table.item(row, col)
                    row_data.append(item.text() if item else "")
                data.append(row_data)
            export_to_csv(filename, columns, data)

    def load_query_from_history(self, item):
        self.sql_editor.setText(item.text())
