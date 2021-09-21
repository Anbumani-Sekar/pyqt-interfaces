from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import *

import sys
class MessageBox(QMessageBox):
    def __init__(self):
        QMessageBox.__init__(self)
        self.setText("No Data, so nothing to show")
        self.setInformativeText("Aviod this ,Don't try this next  at instance")
        self.setIcon(QMessageBox.Warning)
        self.setStandardButtons(QMessageBox.Close)
app = QApplication(sys.argv)
screen = MessageBox()
screen.show()
sys.exit(app.exec_())
