import sys
from PySide2.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("My Form")

        # create widgets
        self.edit = QLineEdit("Write my name here...")
        self.button = QPushButton("Show Greetings")

        # create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        # set dialog layout
        self.setLayout(layout)

        # Add button signal to greetings slot
        self.button.clicked.connect(self.greetings)

    def greetings(self):
        print("Hello {}".format(self.edit.text()))


if __name__ == '__main__':
    # create the Qt Application
    app = QApplication(sys.argv)
    
    # create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())