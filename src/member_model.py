from PyQt5.QtCore import QAbstractTableModel, Qt, pyqtSignal


class MemberModel(QAbstractTableModel):
    data_updated = pyqtSignal()

    def __init__(self, headers=None, read_only_cols=None):
        super().__init__()
        self._table_data = []
        self._headers = headers or []
        self._read_only_cols = read_only_cols or []

    @property
    def headers(self):
        return self._headers[:]

    def insert_row(self):
        self._table_data.append(["" for _ in self._headers])
        self.layoutChanged.emit()
        self.data_updated.emit()

    def __len__(self):
        return len(self._table_data)

    def update_member(self, name, year, num_lessons):
        self._table_data.append(["" for _ in self._headers])
        self._table_data[~0][0] = name
        self._table_data[~0][1] = year
        self._table_data[~0][4] = num_lessons
        self.layoutChanged.emit()
        self.data_updated.emit()

    # Qt model API - do not use directly from outside

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
        if role != Qt.ItemDataRole.EditRole or index.column() in self._read_only_cols:
            return False
        self._table_data[index.row()][index.column()] = (
            value.strip() if isinstance(value, str) else value
        )
        return True

    def flags(self, index):
        if index.column() in self._read_only_cols:
            return Qt.ItemIsSelectable | Qt.ItemIsEnabled
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable
