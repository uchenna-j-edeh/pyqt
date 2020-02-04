from PySide2.QtWidgets import (
    QHBoxLayout,
    QHeaderView,
    QSizePolicy, QTableView, QWidget
)

from custom_tables_model import CustomTableModel

class widget(QWidget):
    def __init__(self, data):
        QWidget.__init__(self)

        self.model = CustomTableModel(data)

        self.table_view = QTableView()
        self.table_view.setModel(self.model)

        self.horizontal_header = self.table_view.horizontalHeader()
        self.vertical_header = self.table_view.verticalHeader()
        self.horizontal_header.setSectionResizeMode(QHeaderView.ResizeToContents)

        self.vertical_header.setSectionResizeMode(QHeaderView.ResizeToContents)

        self.horizontal_header.setStretchLastSection(True)

        self.main_layout = QHBoxLayout()
        size = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        size.setHorizontalStretch(1)
        self.table_view.setSizePolicy(size)
        self.main_layout.addWidget(self.table_view)

        self.setLayout(self.main_layout)