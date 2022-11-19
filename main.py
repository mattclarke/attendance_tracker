import os
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QHeaderView

from member_model import MemberModel


def create_gui():
    basedir = os.path.dirname(__file__)
    window = uic.loadUi(os.path.join(basedir, "mainwindow.ui"))
    model = MemberModel(["Name", "Birth year", "Grade", "Last graded", "Notes"])
    model.insert_row()
    model.insert_row()
    window.table_members.setModel(model)
    window.table_members.horizontalHeader().setSectionResizeMode(
        QHeaderView.Interactive
    )
    window.table_members.horizontalHeader().setStretchLastSection(True)
    return window


if __name__ == "__main__":
    basedir = os.path.dirname(__file__)
    app = QApplication(sys.argv)
    window = create_gui()
    window.show()
    app.exec_()
