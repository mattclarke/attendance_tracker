from PyQt5.QtCore import QAbstractTableModel


class MemberModel(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self._table_data = []

    def insert_row(self):
        self._table_data.append([])

    def __len__(self):
        return len(self._table_data)


def test_can_add_row_to_model():
    model = MemberModel()
    model.insert_row()

    assert len(model) == 1
