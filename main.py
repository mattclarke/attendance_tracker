import os
import sys

from PyQt5 import QtWidgets, uic

from member_model import MemberModel

if __name__ == "__main__":
    basedir = os.path.dirname(__file__)
    app = QtWidgets.QApplication(sys.argv)
    window = uic.loadUi(os.path.join(basedir, "mainwindow.ui"))
    model = MemberModel(["Name", "Birth year", "Grade", "Last graded"])
    window.table_members.setModel(model)
    window.show()
    app.exec_()
