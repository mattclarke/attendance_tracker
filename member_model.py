from PyQt5.QtCore import QAbstractTableModel, Qt


class MemberModel(QAbstractTableModel):
    def __init__(self, headers=None):
        super().__init__()
        self._table_data = []
        self._headers = headers or []

    @property
    def headers(self):
        return self._headers[:]

    def insert_row(self):
        self._table_data.append(["" for _ in self._headers])

    def __len__(self):
        return len(self._table_data)

    def headerData(self, section, orientation=None, role=None):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._headers[section]
        if role == Qt.DisplayRole and orientation == Qt.Vertical:
            return f"{section + 1}"

    def rowCount(self, index=None):
        return len(self._table_data)

    def columnCount(self, index=None):
        return len(self._headers)

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole or role == Qt.ItemDataRole.EditRole:
            return self._table_data[index.row()][index.column()]

    def setData(self, index, value, role):
        if role != Qt.ItemDataRole.EditRole:
            return False
        self._table_data[index.row()][index.column()] = value.strip()
        return True

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable
