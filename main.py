import os
import pathlib
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QHeaderView, QMainWindow

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
        excel_file = pathlib.Path(__file__).parent / "tests" / "Oversikt_example.xlsx"
        data = extract_from_excel_file(excel_file)
        for name, year, num_lessons in data:
            self.model.insert_row()
            self.model._table_data[~0][0] = name
            self.model._table_data[~0][1] = year
            self.model._table_data[~0][4] = num_lessons
        self.table_members.resizeColumnsToContents()


if __name__ == "__main__":
    basedir = os.path.dirname(__file__)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
