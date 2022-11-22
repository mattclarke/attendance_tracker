import os
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import (
    QApplication,
    QFileDialog,
    QHeaderView,
    QMainWindow,
    QMessageBox,
)

from src.member_model import MemberModel
from src.utils import extract_from_excel_file

basedir = os.path.dirname(__file__)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi(os.path.join(basedir, "mainwindow.ui"), self)
        self.btn_import.clicked.connect(self.import_data)
        self._initialise_table()

    def _initialise_table(self):
        self.model = MemberModel(
            [
                "Name",
                "Birth year",
                "Grade",
                "Last graded",
                "# lessons\nsince grading",
                "Notes",
            ],
            [0, 1],
        )
        self.table_members.setModel(self.model)
        self.table_members.horizontalHeader().setSectionResizeMode(
            QHeaderView.Interactive
        )
        self.table_members.horizontalHeader().setStretchLastSection(True)
        self.table_members.resizeColumnsToContents()

    def import_data(self):
        try:
            filters = "Excel files (*.xlsx);;All files (*.*)"
            filename, _ = QFileDialog.getOpenFileName(self, filter=filters)
            data = extract_from_excel_file(filename)
            for name, year, num_lessons in data:
                self.model.update_member(name, year, num_lessons)
            self.table_members.resizeColumnsToContents()
        except Exception as error:
            QMessageBox.critical(
                self, "Import Error", f"Could not import data from file: {error}"
            )


if __name__ == "__main__":
    basedir = os.path.dirname(__file__)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
