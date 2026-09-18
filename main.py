import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QPushButton, QFileDialog, QMessageBox
from queries.accounts import get_accounts
from imports.csv_import import import_csv


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Personal Finance Tracker")

        self.account_dropdown = QComboBox()
        for account in get_accounts():
            self.account_dropdown.addItem(account.AccountName, account.AccountID)

        self.import_button = QPushButton("Import CSV")
        self.import_button.clicked.connect(self.handle_import)

        layout = QVBoxLayout()
        layout.addWidget(self.account_dropdown)
        layout.addWidget(self.import_button)
        self.setLayout(layout)

    def handle_import(self):
        account_id = self.account_dropdown.currentData()
        file_path, _ = QFileDialog.getOpenFileName(self, "Select CSV", "", "CSV Files (*.csv)")
        if not file_path:
            return

        try:
            imported, skipped = import_csv(file_path, account_id)
        except ValueError as e:
            QMessageBox.warning(self, "Import Error", str(e))
            return

        QMessageBox.information(
            self, "Import Complete",
            f"Imported {imported} new transaction(s). Skipped {skipped} duplicate(s)."
        )


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())