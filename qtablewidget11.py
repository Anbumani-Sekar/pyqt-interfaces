from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import sys
class Window(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.setWindowTitle("HELLO")
        layout = QGridLayout()
        self.setLayout(layout)
           
        self.tablewidget = QTableWidget()
        self.tablewidget.setRowCount(2)
        self.tablewidget.setColumnCount(2)
        
        self.tablewidget.setItem(0,0,  QTableWidgetItem())

        self.tablewidget.setItem(0,1, QTableWidgetItem())
        self.tablewidget.setItem(1,0, QTableWidgetItem())
        self.tablewidget.setItem(1,1, QTableWidgetItem())
    
        self.button = QPushButton("button")
        self.button.setToolTip('click me')
        self.button.clicked.connect(self.on_button_clicked)
        layout.addWidget(self.button, 1, 0)
        layout.addWidget(self.tablewidget, 0, 0)

    def on_button_clicked(self):
            self.itemChanged.connect(self.getData)
    def getData(self):
        data=[]
        for row in range(4):
            row_data=[]
            for col in range(2):
                if self.item(row,col):
                    text=self.item(row,col).text()
                    row_data.append(str(text))
                else:
                    row_data.append("")
            data.append(row_data)
        global DATA
        DATA=data
        print(data)
        print(DATA)
        '''self.tablewidget.setItem(0,0, QTableWidgetItem("cell(1,1)"))
        self.tablewidget.setItem(0,1, QTableWidgetItem("cell(1,2)"))
        self.tablewidget.setItem(0,2, QTableWidgetItem("cell(1,3)"))
        self.tablewidget.setItem(1,0, QTableWidgetItem("cell(2,1)"))
        self.tablewidget.setItem(1,1, QTableWidgetItem("cell(2,2)"))
        self.tablewidget.setItem(1,2, QTableWidgetItem("cell(2,3)"))
        self.tablewidget.setItem(2,0, QTableWidgetItem("cell(3,1)"))
        self.tablewidget.setItem(2,1, QTableWidgetItem("cell(3,2)"))
        self.tablewidget.setItem(2,2, QTableWidgetItem("cell(3,3)"))'''
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
        
