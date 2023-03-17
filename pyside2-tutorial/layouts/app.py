import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget
from PySide2.QtGui import QPalette, QColor

class Color(QWidget):
    """In this code we subclass QWidget to create our own custom widget Color. 
    We accept a single parameter when creating the widget — color (a str). 
    We first set .setAutoFillBackground to True to tell 
    the widget to automatically fill its background with the window cooler. 
    Next we get the current palette 
    (which is the global desktop palette by default) and change the 
    current QPalette.Window color to a new QColor described by the value color 
    we passed in. Finally we apply this palette back to the widget. 
    The end result is a widget that is filled with a solid color, that 
    we specified when we created it.

    Args:
        QWidget (_type_): _description_
    """

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

        widget = Color('red')
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()