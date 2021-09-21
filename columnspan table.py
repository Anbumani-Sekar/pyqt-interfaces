import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QBrush,QColor 



class Table(QWidget):
    def _init_(self,parent=None):
        super.__init__(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("qt")
        self.resize(660,300);
        self.setLayout(conLayout)

        conLayout=QHBoxLayout()

        self.tablewidget=QTableView()
        self.tablewidget.setRowCount(7)
        self.tablewidget.setColumnCount(6)
        conLayout.addWidget(self.tablewidget)

        self.tablewidget.horizontalHeader().setVisible(False)
        self.tablewidget.verticalHeader().setVisible(False)

        self.tablewidget.setSpan(self,0,0,1,6)
        self.newItem=QTableWidgetItem("tablewidget.setSpan(0,0,1,6)")
        self.tablewidget.setItem(3,0,self.newItem)

        self.newItem=QTableWidgetItem("hello")
        self.newItem.Foreground(QBrush(QColor(0,255,0)))
        self.tablewidget.setItem(3,1,self.newItem)

        
        self.newItem=QTableWidgetItem("pythonff")
        self.newItem.Foreground(QBrush(QColor(255,0,0)))
        self.tablewidget.setItem(3,1,self.newItem)
        
        self.setLayout(conLayout)

app = QApplication(sys.argv)
screen = Table()
screen.show()
sys.exit(app.exec_())






        

