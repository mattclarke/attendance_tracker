from PyQt5.QtCore import Qt

from src.member_model import MemberModel


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


def test_can_add_new_members():
    headers = [
        "Name",
        "Birth year",
        "Grade",
        "Last graded",
        "# lessons\nsince grading",
        "Notes",
    ]
    model = MemberModel(headers=headers)

    model.update_member("John Smith", "1985", 12)

    assert (
        model.data(model.createIndex(0, 0), Qt.ItemDataRole.DisplayRole) == "John Smith"
    )
    assert model.data(model.createIndex(0, 1), Qt.ItemDataRole.DisplayRole) == "1985"
    assert model.data(model.createIndex(0, 4), Qt.ItemDataRole.DisplayRole) == 12


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


def test_qt_can_edit_data():
    headers = ["column1", "column2", "column3"]
    model = MemberModel(headers=headers)
    model.insert_row()

    model.setData(model.createIndex(0, 1), "Hello", Qt.ItemDataRole.EditRole)

    assert model.data(model.createIndex(0, 1), Qt.ItemDataRole.DisplayRole) == "Hello"


def test_qt_cannot_edit_specified_columns():
    headers = ["column1", "column2", "column3"]
    model = MemberModel(headers=headers, read_only_cols=[0])
    model.insert_row()

    model.setData(model.createIndex(0, 0), "Hello", Qt.ItemDataRole.EditRole)

    assert model.data(model.createIndex(0, 0), Qt.ItemDataRole.DisplayRole) == ""
