from PyQt5.QtCore import Qt

from src.member_model import MemberModel
from src.utils import convert_table_to_clipboard_format


def test_can_copy_table_data_to_clipboard():
    model = MemberModel()
    model.update_members(
        [("Adam", "1977", 5), ("Bea", "1987", 15), ("Carlo", "1997", 25)]
    )

    result = convert_table_to_clipboard_format(model)

    assert (
        result
        == "Adam\t1977\t\t\t\t5\t\nBea\t1987\t\t\t\t15\t\nCarlo\t1997\t\t\t\t25\t"
    )


def test_blank_lines_skipped():
    model = MemberModel()
    model.update_members(
        [("Adam", "1977", 5), ("Bea", "1987", 15), ("Carlo", "1997", 25)]
    )

    for col in range(model.columnCount()):
        model.setData(model.createIndex(1, col), "", Qt.ItemDataRole.EditRole)

    result = convert_table_to_clipboard_format(model)

    assert result == "Adam\t1977\t\t\t\t5\t\nCarlo\t1997\t\t\t\t25\t"
