from PyQt5.QtWidgets import *
import sys
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.combobox = QComboBox()
        self.combobox.addItem("course Objective 1")
        self.combobox.addItem("course Objective 2")
        self.combobox.addItem("course Objective 3")
        self.combobox.addItem("course Objective 4")
        self.combobox.addItem("course Objective 5")

        self.combobox.currentTextChanged.connect(self.combobox_changed)
        layout.addWidget(self.combobox)
    def combobox_changed(self):
        text = self.combobox.currentText()
        print(text)
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
