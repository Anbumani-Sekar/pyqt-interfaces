from PyQt5.QtWidgets import *
import sys
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.toolbar = QToolBar()
        self.layout.addWidget(self.toolbar)
        self.toolbutton1 = QToolButton()
        self.toolbutton1.setText("Button 1")
        
        self.toolbar.addWidget(self.toolbutton1)
        self.toolbutton2 = QToolButton()
        self.toolbutton2.setText("Button 2")
        
        self.toolbar.addWidget(self.toolbutton2)
        self.toolbutton1.clicked.connect(self.butclick)
    def butclick(self):
        print("its work")
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
