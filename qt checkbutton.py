from PyQt5.QtWidgets import *
import sys
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.checkbox1 = QCheckBox("PART-A")
        self.checkbox1.setChecked(False)
        self.checkbox1.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox1, 0, 0)
        self.checkbox2 = QCheckBox("PART-B")
        self.checkbox2.setChecked(False)

        self.checkbox2.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox2, 1, 0)
        self.checkbox3 = QCheckBox("PART-C")
        self.checkbox3.setChecked(False)

        self.checkbox3.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox3, 2, 0)
    def checkbox_toggled(self):
        selected = []
        if self.checkbox1.isChecked():
            selected.append(1)
        if self.checkbox2.isChecked():
            selected.append(2)
        if self.checkbox3.isChecked():
            selected.append(3)
        print(selected)
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
