import os
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QHeaderView, QMainWindow

from src.member_model import MemberModel

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
                "# lessons since grading",
                "Notes",
            ],
            [0, 1],
        )
        self.model.insert_row()
        self.model.insert_row()
        self.table_members.setModel(self.model)
        self.table_members.horizontalHeader().setSectionResizeMode(
            QHeaderView.Interactive
        )
        self.table_members.horizontalHeader().setStretchLastSection(True)
        self.table_members.resizeColumnsToContents()

    def import_data(self):
        pass


if __name__ == "__main__":
    basedir = os.path.dirname(__file__)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
