from PyQt5.QtWidgets import *
import sys
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("HELLO")
        layout = QGridLayout()
        self.setLayout(layout)
        label = QLabel("0, 0!")
        layout.addWidget(label, 0, 0)
        label = QLabel("1, 0!")
        layout.addWidget(label, 1, 0)
        label = QLabel("0, 1!")
        layout.addWidget(label, 0, 1)
        label = QLabel("1, 1!")
        layout.addWidget(label, 1, 1)
        label = QLabel("1, 2!")
        layout.addWidget(label, 1, 2)
        label = QLabel("2, 1!")
        layout.addWidget(label, 2, 1)
        label = QLabel("0, 2!")
        layout.addWidget(label, 0, 2)
        label = QLabel("2, 0!")
        layout.addWidget(label, 2, 0)
        label = QLabel("2, 2!")
        layout.addWidget(label, 2, 2)



app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())

