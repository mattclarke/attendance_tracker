from PyQt5.QtCore import Qt

from member_model import MemberModel


def test_can_add_row_to_model():
    model = MemberModel()
    model.insert_row()

    assert len(model) == 1


def test_defaults_to_no_headers():
    model = MemberModel()

    assert len(model.headers) == 0


def test_can_define_headers():
    headers = ["column1", "column2", "column3"]
    model = MemberModel(headers=headers)

    assert model.headers == headers


def test_qt_can_access_headers():
    headers = ["column1", "column2", "column3"]
    model = MemberModel(headers=headers)

    model.insert_row()
    model.insert_row()
    model.insert_row()

    assert model.headerData(0, Qt.Horizontal, Qt.DisplayRole) == headers[0]
    assert model.headerData(1, Qt.Horizontal, Qt.DisplayRole) == headers[1]
    assert model.headerData(2, Qt.Horizontal, Qt.DisplayRole) == headers[2]

    assert model.headerData(0, Qt.Vertical, Qt.DisplayRole) == "1"
    assert model.headerData(1, Qt.Vertical, Qt.DisplayRole) == "2"
    assert model.headerData(2, Qt.Vertical, Qt.DisplayRole) == "3"


def test_qt_can_get_row_count_empty():
    headers = ["column1", "column2", "column3"]
    model = MemberModel(headers=headers)

    assert model.rowCount() == 0


def test_qt_can_get_row_count():
    headers = ["column1", "column2", "column3"]
    model = MemberModel(headers=headers)

    model.insert_row()
    model.insert_row()

    assert model.rowCount() == 2


def test_qt_can_get_column_count():
    headers = ["column1", "column2", "column3"]
    model = MemberModel(headers=headers)

    assert model.columnCount() == 3


def test_qt_can_get_data():
    headers = ["column1", "column2", "column3"]
    model = MemberModel(headers=headers)

    model._table_data.append(["one", "two", "three"])
    model._table_data.append(["four", "five", "six"])

    assert model.data(model.createIndex(0, 0), Qt.ItemDataRole.DisplayRole) == "one"
    assert model.data(model.createIndex(1, 1), Qt.ItemDataRole.DisplayRole) == "five"
