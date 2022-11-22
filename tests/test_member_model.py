from PyQt5.QtCore import Qt

from src.member_model import HEADERS, MemberModel


def test_can_add_row_to_model():
    model = MemberModel()
    model.insert_row()

    assert len(model) == 1


def test_headers_are_set():
    model = MemberModel()

    assert model.headers == HEADERS


def test_can_add_new_members():
    model = MemberModel()

    model.update_member("John Smith", "1985", 12)

    assert (
        model.data(model.createIndex(0, 0), Qt.ItemDataRole.DisplayRole) == "John Smith"
    )
    assert model.data(model.createIndex(0, 1), Qt.ItemDataRole.DisplayRole) == "1985"
    assert model.data(model.createIndex(0, 4), Qt.ItemDataRole.DisplayRole) == 12


def test_qt_can_access_headers():
    model = MemberModel()

    model.insert_row()
    model.insert_row()
    model.insert_row()

    assert model.headerData(0, Qt.Horizontal, Qt.DisplayRole) == HEADERS[0]
    assert model.headerData(1, Qt.Horizontal, Qt.DisplayRole) == HEADERS[1]
    assert model.headerData(2, Qt.Horizontal, Qt.DisplayRole) == HEADERS[2]
    assert model.headerData(5, Qt.Horizontal, Qt.DisplayRole) == HEADERS[~0]

    assert model.headerData(0, Qt.Vertical, Qt.DisplayRole) == "1"
    assert model.headerData(1, Qt.Vertical, Qt.DisplayRole) == "2"
    assert model.headerData(2, Qt.Vertical, Qt.DisplayRole) == "3"


def test_qt_can_get_row_count_empty():
    model = MemberModel()

    assert model.rowCount() == 0


def test_qt_can_get_row_count():
    model = MemberModel()

    model.insert_row()
    model.insert_row()

    assert model.rowCount() == 2


def test_qt_can_get_column_count():
    model = MemberModel()

    assert model.columnCount() == len(HEADERS)


def test_qt_can_get_data():
    model = MemberModel()

    model._table_data.append(["one", "two", "three"])
    model._table_data.append(["four", "five", "six"])

    assert model.data(model.createIndex(0, 0), Qt.ItemDataRole.DisplayRole) == "one"
    assert model.data(model.createIndex(1, 1), Qt.ItemDataRole.DisplayRole) == "five"


def test_qt_can_edit_data():
    model = MemberModel()
    model.insert_row()

    model.setData(model.createIndex(0, 1), "Hello", Qt.ItemDataRole.EditRole)

    assert model.data(model.createIndex(0, 1), Qt.ItemDataRole.DisplayRole) == "Hello"


def test_qt_cannot_edit_specified_columns():
    model = MemberModel(read_only_cols=[0])
    model.insert_row()

    model.setData(model.createIndex(0, 0), "Hello", Qt.ItemDataRole.EditRole)

    assert model.data(model.createIndex(0, 0), Qt.ItemDataRole.DisplayRole) == ""
