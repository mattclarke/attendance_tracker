import os
import sys

from PyQt6 import uic
from PyQt6.QtCore import QSortFilterProxyModel, Qt
from PyQt6.QtWidgets import (
    QApplication,
    QFileDialog,
    QHeaderView,
    QMainWindow,
    QMessageBox,
)

from src.member_model import MemberModel
from src.utils import Converter, extract_from_excel_file

basedir = os.path.dirname(__file__)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi(os.path.join(basedir, "mainwindow.ui"), self)
        self.clipboard = QApplication.instance().clipboard()
        self.btn_import.clicked.connect(self.import_data)
        self.btn_test.clicked.connect(self.foo)
        self._initialise_table()

    def _initialise_table(self):
        self.model = MemberModel(
            [0, 1],
        )
        proxy_model = QSortFilterProxyModel()
        proxy_model.setSourceModel(self.model)
        self.table_members.setModel(proxy_model)
        self.table_members.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Interactive
        )
        self.table_members.horizontalHeader().setStretchLastSection(True)
        self.table_members.resizeColumnsToContents()
        self.table_members.horizontalHeader().setSortIndicator(
            0, Qt.SortOrder.AscendingOrder
        )
        self.table_members.setSortingEnabled(True)

    def import_data(self):
        try:
            filters = "Excel files (*.xlsx);;All files (*.*)"
            filename, _ = QFileDialog.getOpenFileName(
                self, caption="Select Excel file", filter=filters
            )
            if filename:
                data = extract_from_excel_file(filename)
                self.model.update_members(data)
                self.table_members.resizeColumnsToContents()
        except Exception as error:
            QMessageBox.critical(
                self, "Import Error", f"Could not import data from file: {error}"
            )

    def foo(self):
        self.load()

    def load(self):
        try:
            filters = "JSON file (*.json);;All files (*.*)"
            default = "JSON file (*.json)"
            filename, _ = QFileDialog.getOpenFileName(
                self, caption="Select data file", filter=filters, initialFilter=default
            )
            if filename:
                with open(filename, "r") as file:
                    data = Converter.from_json(file.read())
                self.model.replace_data(data)
                self.table_members.resizeColumnsToContents()
        except Exception as error:
            QMessageBox.critical(
                self, "Load Error", f"Could not load data from file: {error}"
            )

    def save(self):
        try:
            filters = "JSON file (*.json);;All files (*.*)"
            default = "JSON file (*.json)"
            filename, _ = QFileDialog.getSaveFileName(
                self, caption="Save file", initialFilter=default, filter=filters
            )
            if filename:
                as_json = Converter.to_json(list(self.model.members.values()))
                with open(filename, "w") as file:
                    file.write(as_json)
        except Exception as error:
            QMessageBox.critical(
                self, "Save Error", f"Could not save data to file: {error}"
            )


if __name__ == "__main__":
    basedir = os.path.dirname(__file__)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
