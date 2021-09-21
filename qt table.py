from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import PyQt5.QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import sys
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("HELLO")
        self.create()
        
    def create(self):
        
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.tablewidget = QTableWidget()
        self.tablewidget.setRowCount(69)
        self.tablewidget.setColumnCount(3)
        self.tablewidget.rowCount()
        self.tablewidget.columnCount()
        self.tablewidget.setHorizontalHeaderLabels(["REG NO", "CO1", "CO2",])
        self.tablewidget.horizontalHeader()
        self.tablewidget.verticalHeader()
        self.clip=QApplication.clipboard()

        self.setWindowIcon(QIcon('icon.png'))
        self.tablewidget.setItem(0,0, QTableWidgetItem("cell(1,1)"))
        self.tablewidget.setItem(0,1, QTableWidgetItem("cell(1,2)"))
        self.tablewidget.setItem(0,2, QTableWidgetItem("cell(1,3)"))
        self.tablewidget.setItem(1,0, QTableWidgetItem("cell(2,1)"))
        self.tablewidget.setItem(1,1, QTableWidgetItem("cell(2,2)"))
        self.tablewidget.setItem(1,2, QTableWidgetItem("cell(2,3)"))
        self.tablewidget.setItem(2,0, QTableWidgetItem("cell(3,1)"))
        self.tablewidget.setItem(2,1, QTableWidgetItem("cell(3,2)"))
        self.tablewidget.setItem(2,2, QTableWidgetItem("cell(3,3)"))
        self.tablewidget.move(0,0)
        #self.tablewidget.inputMethodQuery(self, Qt.InputMethodQuery) 
  
        #self.tablewidget.alternatingRowColors(True)
        self.layout.addWidget(self.tablewidget, 0, 0)
        self.tablewidget.doubleClicked.connect(self.click)
        self.tablewidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        #self.tablewidget.setEditTriggers(QAbstractItemView.CurrentChanged)
        #print(self.tablewidget.takeItem(0,2)) 
        #a=cellChanged
        #print(self.tablewidget.cellChanged)
        #print(self.tablewidget.setShowGrid(1))
    def click(self):
        #print(self.tablewidget.itemAt( 1, 2,QTableWidgetItem))
        
        print(self.tablewidget.dataChanged)
    def button(self):
        ttt=self.cell
        print(ttt)
    def keypress(self,e):
        if(e.modifiers() & QtCore.Qt.ControlModifier):
            selected = self.table.selectedRanges()

            if e.key() == QtCore.Qt.key_V:#past
                first_row = selected[0].topRow()
                first_col = selected[0].leftcolun()
                for r,row in enumerate(self.clip.text().spilt('\n')):
                    for c, text in enumerate(row.spilt('\t')):
                        self.table.setItem(first_row+r,first_col+c,QtGui.QTableWidgetItem(text))
            elif e.key() == QtCore.Qt.key_C:
                s=" "
                for r in xrange(selected[0].topRow,selected[0].bottomRow()+1):
                    for c in xrange(selected[0].leftColumn(),selected[0].rightColumn()):
                            try:
                                    s += str(self.table.item(r,c).text()) + "\t"
                            except AttributeError:
                                    s += "\t"
                    s= s[:-1]+ "\n"
                self.clipsetText(s)
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
