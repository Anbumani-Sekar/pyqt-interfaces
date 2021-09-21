from PyQt5.QtWidgets import *
import sys
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.buttongroup = QButtonGroup()
        self.buttongroup.setExclusive(True)
        self.buttongroup.buttonClicked[int].connect(self.on_button_clicked)
        button = QPushButton("Button 1")
        self.buttongroup.addButton(button, 1)
        layout.addWidget(button)
        button = QPushButton("Button 2")
        self.buttongroup.addButton(button, 2)
        layout.addWidget(button)
    def on_button_clicked(self, id):
        for button in self.buttongroup.buttons():
            if button is self.buttongroup.button(id):
                print("%s was clicked!" % (button.text()))
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
