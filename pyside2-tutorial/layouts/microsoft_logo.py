import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
from PySide2.QtGui import QPalette, QColor

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layoutg = QVBoxLayout()
        layout1 = QVBoxLayout()
        layout2 = QVBoxLayout()
        layouta = QHBoxLayout()
        layoutb = QHBoxLayout()

        layoutg.setContentsMargins(0,0,0,0)
        layoutg.setSpacing(5)


        layouta.addWidget(Color('#F25022'))
        layouta.addWidget(Color('#7FBA00'))

        layout1.addLayout( layouta )
        layoutg.addLayout(layout1)

        layoutb.addWidget(Color('#00A4EF'))
        layoutb.addWidget(Color('#FFB900'))

        layout2.addLayout( layoutb )
        layoutg.addLayout(layout2)

        widget = QWidget()
        widget.setLayout(layoutg)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()