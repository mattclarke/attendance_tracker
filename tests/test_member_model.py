from PyQt6.QtCore import Qt

from src.member_model import HEADERS, Member, MemberModel


def test_can_add_row_to_model():
    model = MemberModel()
    model.update_members([("Adam", "1977", 5)])

    assert len(model) == 1


def test_headers_are_set():
    model = MemberModel()

    assert model.headers == HEADERS


def test_can_add_new_members():
    model = MemberModel()

    model.update_members([("John Smith", "1985", 12)])

    assert (
        model.data(model.createIndex(0, 0), Qt.ItemDataRole.DisplayRole) == "John Smith"
    )
    assert model.data(model.createIndex(0, 1), Qt.ItemDataRole.DisplayRole) == "1985"
    assert model.data(model.createIndex(0, 5), Qt.ItemDataRole.DisplayRole) == 12


def test_can_get_members():
    model = MemberModel()

    model.update_members([("John Smith", "1985", 12)])
    model.update_members([("Jane Doe", "1995", 35)])

    members = model.get_members()

    assert members[("John Smith", "1985")] == Member(
        "John Smith", "1985", "", "", "", 12, ""
    )
    assert members[("Jane Doe", "1995")] == Member(
        "Jane Doe", "1995", "", "", "", 35, ""
    )


def test_qt_can_access_headers():
    model = MemberModel()

    model.update_members(
        [("Adam", "1977", 5), ("Bea", "1987", 15), ("Carlo", "1997", 25)]
    )

    assert (
        model.headerData(0, Qt.Orientation.Horizontal, Qt.ItemDataRole.DisplayRole)
        == HEADERS[0]
    )
    assert (
        model.headerData(1, Qt.Orientation.Horizontal, Qt.ItemDataRole.DisplayRole)
        == HEADERS[1]
    )
    assert (
        model.headerData(2, Qt.Orientation.Horizontal, Qt.ItemDataRole.DisplayRole)
        == HEADERS[2]
    )
    assert (
        model.headerData(6, Qt.Orientation.Horizontal, Qt.ItemDataRole.DisplayRole)
        == HEADERS[~0]
    )


def test_qt_can_get_row_count_empty():
    model = MemberModel()

    assert model.rowCount() == 0


def test_qt_can_get_row_count():
    model = MemberModel()

    model.update_members(
        [("Adam", "1977", 5), ("Bea", "1987", 15), ("Carlo", "1997", 25)]
    )

    assert model.rowCount() == 3


def test_qt_can_get_column_count():
    model = MemberModel()

    assert model.columnCount() == len(HEADERS)


def test_qt_can_get_data():
    model = MemberModel()

    model.update_members(
        [("Adam", "1977", 5), ("Bea", "1987", 15), ("Carlo", "1997", 25)]
    )

    assert model.data(model.createIndex(0, 0), Qt.ItemDataRole.DisplayRole) == "Adam"
    assert model.data(model.createIndex(1, 1), Qt.ItemDataRole.DisplayRole) == "1987"


def test_qt_can_edit_data():
    model = MemberModel()
    model.update_members(
        [("Adam", "1977", 5), ("Bea", "1987", 15), ("Carlo", "1997", 25)]
    )

    model.setData(model.createIndex(0, 5), 123, Qt.ItemDataRole.EditRole)

    assert model.data(model.createIndex(0, 5), Qt.ItemDataRole.DisplayRole) == 123


def test_qt_cannot_edit_specified_columns():
    model = MemberModel(read_only_cols=[0])
    model.update_members([("Adam", "1977", 5)])

    model.setData(model.createIndex(0, 0), "John", Qt.ItemDataRole.EditRole)

    assert model.data(model.createIndex(0, 0), Qt.ItemDataRole.DisplayRole) == "Adam"


def test_editing_value_updates_member():
    model = MemberModel()
    model.update_members(
        [("Adam", "1977", 5), ("Bea", "1987", 15), ("Carlo", "1997", 25)]
    )

    model.setData(model.createIndex(0, 5), 123, Qt.ItemDataRole.EditRole)

    assert model.members[("Adam", "1977")].lessons == 123


def test_updating_members_with_existing_member_increments_lessons():
    model = MemberModel()
    model.update_members(
        [("Adam", "1977", 5), ("Bea", "1987", 15), ("Carlo", "1997", 25)]
    )

    model.update_members([("Adam", "1977", 2)])

    assert model.members[("Adam", "1977")].lessons == 7
    assert len(model.table_data) == 3
    assert model.table_data[0][5] == 7


def test_when_updating_it_returns_new_members():
    pass
