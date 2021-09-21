from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.Qt import *
from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
from PyQt5.QtGui import QImage, QPainter
from PyQt5.QtCore import QFile
 

class Window(QWidget):
   def __init__(self):
       QWidget.__init__(self)
       layout = QGridLayout()
       self.setLayout(layout)
       menubar = QMenuBar()
       layout.addWidget(menubar, 0, 0)
       actionFile = menubar.addMenu("File")
       actionFile.addAction("New")
       actionFile.triggered.connect(lambda: self.copyByContext(event))

       actionFile.addSeparator()
       actionFile.addAction("Quit")
       menubar.addMenu("Edit")
       menubar.addMenu("View")
       menubar.addMenu("Help")
       self.tableView = QtWidgets.QTableView(self)
       #self.tableView.horizontalHeader().setStretchLastSection(True)
       self.tableView.setShowGrid(True)
       self.tableView.setGeometry(10, 50, 780, 645)
 
      
       grid = QtWidgets.QGridLayout()
       
       grid.addWidget(self.tableView, 1, 0, 1, 9)
       self.setLayout(grid)
 
       
 
  
   
   
       #def contextMenuEvent(self, event):
       
       self.menu = QtWidgets.QMenu('fff',self)
       grid.addWidget(self.menu,0,0)
       # copy
       copyAction = QtWidgets.QAction('Copy', self)
       copyAction.triggered.connect(lambda: self.copyByContext(event))
       # paste
       pasteAction = QtWidgets.QAction('Paste', self)
       pasteAction.triggered.connect(lambda: self.pasteByContext(event))
       # cut
       cutAction = QtWidgets.QAction('Cut', self)
       cutAction.triggered.connect(lambda: self.cutByContext(event))
       # delete selected Row
       removeAction = QtWidgets.QAction('delete Row', self)
       removeAction.triggered.connect(lambda: self.deleteRowByContext(event))
       # add Row after
       addAction = QtWidgets.QAction('insert new Row after', self)
       addAction.triggered.connect(lambda: self.addRowByContext(event))
       # add Row before
       addAction2 = QtWidgets.QAction('insert new Row before', self)
       addAction2.triggered.connect(lambda: self.addRowByContext2(event))
       # add Column before
       addColumnBeforeAction = QtWidgets.QAction('insert new Column before', self)
       addColumnBeforeAction.triggered.connect(lambda: self.addColumnBeforeByContext(event))
       # add Column after
       addColumnAfterAction = QtWidgets.QAction('insert new Column after', self)
       addColumnAfterAction.triggered.connect(lambda: self.addColumnAfterByContext(event))
       # delete Column
       deleteColumnAction = QtWidgets.QAction('delete Column', self)
       deleteColumnAction.triggered.connect(lambda: self.deleteColumnByContext(event))
       # add other required actions
       self.menu.addAction(copyAction)
       self.menu.addAction(pasteAction)
       self.menu.addAction(cutAction)
       self.menu.addSeparator()
       self.menu.addAction(addAction)
       self.menu.addAction(addAction2)
       self.menu.addSeparator()
       self.menu.addAction(addColumnBeforeAction)
       self.menu.addAction(addColumnAfterAction)
       self.menu.addSeparator()
       self.menu.addAction(removeAction)
       self.menu.addAction(deleteColumnAction)
       #self.menu.popup(QtGui.QCursor.pos())
 
   def deleteRowByContext(self, event):
      pass

   def addRowByContext(self, event):
      pass

   def addRowByContext2(self, event):
      pass

   def addColumnBeforeByContext(self, event):
      pass

   def addColumnAfterByContext(self, event):
      pass

   def deleteColumnByContext(self, event):
      pass

   def copyByContext(self, event):
      pass
   def pasteByContext(self, event):
      pass

 
   def cutByContext(self, event):
      pass
      

 
if __name__ == "__main__":
   import sys
 
   app = QtWidgets.QApplication(sys.argv)
   #app.setApplicationName('MyWindow')
   main = Window()
   main.setMinimumSize(820, 300)
   main.setGeometry(0,0,820,700)
   main.setWindowTitle("CSV Viewer")
   main.show()
 
sys.exit(app.exec_())
