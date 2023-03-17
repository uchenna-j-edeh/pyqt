import sys
from PySide2.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

# In Qt any widgets can be windows. For example, if you replace QtWidget with QPushButton. 
# In the example below, you would get a window with a single push-able button in it.
window = QPushButton("Push Me")
window.show()

app.exec_()