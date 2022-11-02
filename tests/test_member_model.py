from PyQt5.QtCore import QAbstractTableModel


class MemberModel(QAbstractTableModel):
    def __init__(self, headers=None):
        super().__init__()
        self._table_data = []
        self._headers = headers or []

    @property
    def headers(self):
        return self._headers[:]

    def insert_row(self):
        self._table_data.append([])

    def __len__(self):
        return len(self._table_data)

    def headerData(self, section, orientation=None, role=None):
        return self._headers[section]


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


def test_headers_can_be_accessed_qt_style():
    headers = ["column1", "column2", "column3"]
    model = MemberModel(headers=headers)

    assert model.headerData(0) == headers[0]
    assert model.headerData(1) == headers[1]
    assert model.headerData(2) == headers[2]
