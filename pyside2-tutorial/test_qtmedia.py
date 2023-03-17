import os

from PySide2 import QtMultimedia
from PySide2 import QtWidgets, QtMultimedia

av_path = "/Users/uchennaedeh/Downloads/IMG_1822.MOV"

if not os.path.exists(av_path):
    sys.stdout.write(f"{av_path} does not exist")

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mediaPlayer = QtMultimedia.QMediaPlayer(self)
        self.mediaPlayer.setMedia(QtMultimedia.QMediaContent(av_path))
        self.mediaPlayer.play()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
