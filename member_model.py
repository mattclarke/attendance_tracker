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
