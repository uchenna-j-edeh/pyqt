import sys
from PySide2.QtWidgets import (
    QMainWindow, QApplication,
    QCheckBox
)
from PySide2.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        widget = QCheckBox()
        widget.setCheckState(Qt.Checked)

        # For tristate: widget.setCheckState(Qt.PartiallyChecked)
        # Or: widget.setTriState(True)
        widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(widget)


    def show_state(self, s):
        print(s == Qt.Checked)
        print(s)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()