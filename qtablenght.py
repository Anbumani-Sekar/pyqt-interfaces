from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
import io
import csv
from PyQt5.Qt import *
import sys
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("HELLO")
        layout = QGridLayout()
        self.setLayout(layout)
        self.tablewidget2 = QTableWidget()
        self.r=100
        self.c=100
        self.tablewidget2.setRowCount(self.r)
        self.tablewidget2.setColumnCount(self.c)
        self.tablewidget2.setStyleSheet("QTableView {selection-background-color: yellow;}");

        self.tablewidget2.itemChanged.connect(self.getData)
        layout.addWidget(self.tablewidget2, 4, 0)
        self.button =  QPushButton()
        self.button.setText("load data")

        self.button.setToolTip('data print')
        self.button.clicked.connect(self.ldfile)
        layout.addWidget(self.button)
        self.button =  QPushButton()
        self.button.setText("save data")

        self.button.setToolTip('data print')
        self.button.clicked.connect(self.sefile)
        layout.addWidget(self.button)
    def   ldfile(self):
        loadfile=QFileDialog.getOpenFileName(self,"Openn File","./","All files(*)")
        if loadfile:
            with open(loadfile,"r")as loaddata:
                data=eval(loaddata.read())

            #Table().filling(data)
    def   sefile(self):
        savefile=QFileDialog.getSaveFileName(self,"save File","./","All files(*)")
        if savefile:
            with open(savefile,"w")as savedata:
                savedata.write(repr(DATA))
    def getData(self):
        

        data=[]
        for row in range(0,100):
            row_data=[]
            for col in range(100):
                if self.tablewidget2.item(row,col):
                    text=self.tablewidget2.item(row,col).text()
                    row_data.append((text))
                else:
                    row_data.append("")
            data.append(row_data)
        
        self.data=data
        #print(self.data)
    
    def keyPressEvent(self, ev):
        if (ev.key() == Qt.Key_C) and (ev.modifiers() & Qt.ControlModifier): 
            self.copySelection()
        if (ev.key() == Qt.Key_V) and (ev.modifiers() & Qt.ControlModifier): 
            self.pasteSelection()

    def copySelection(self):
        selection = self.tablewidget2.selectedIndexes()
        data=self.data
        if selection:
            rows = sorted(index.row() for index in selection)
            columns = sorted(index.column() for index in selection)
            rowcount = rows[-1] - rows[0] + 1
            colcount = columns[-1] - columns[0] + 1
            table = [[''] * colcount for _ in range(rowcount)]
            for index in selection:
                row = index.row() - rows[0]
                column = index.column() - columns[0]
                table[row][column] = index.data()
                
            stream = io.StringIO()
            csv.writer(stream, delimiter='\t').writerows(table)
            QApplication.clipboard().setText(stream.getvalue())
        
    def pasteSelection(self):
        selection = self.tablewidget2.selectedIndexes()
        if selection:
            model = self.tablewidget2.model()
            buffer = QApplication.clipboard().text()
            print(buffer)

            rows = sorted(index.row() for index in selection)
            columns = sorted(index.column() for index in selection)
            
            reader = csv.reader(io.StringIO(buffer), delimiter='\t')
            if len(rows) == 1 and len(columns) == 1:
                for i, line in enumerate(reader):
                    for j, cell in enumerate(line):
                        model.setData(model.index(rows[0]+i,columns[0]+j), cell)
            else:
                arr = [ [ cell for cell in row ] for row in reader]
                for index in selection:
                    row = index.row() - rows[0]
                    column = index.column() - columns[0]
                    model.setData(model.index(index.row(), index.column()), arr[row][column])

    '''def pasteSelection(self):
        selection = self.tablewidget2.selectedIndexes()
        if selection:
            #model = self.tablewidget2()
            buffer = QApplication.clipboard().text()
            print(buffer)
            rows = sorted(index.row() for index in selection)
            #print(rows)
            columns = sorted(index.column() for index in selection)
            #print(columns)
            reader = csv.reader(io.StringIO(buffer), delimiter='\t')
            if len(rows) == 1 and len(columns) == 1:
                for i, line in enumerate(reader):
                    for j, cell in enumerate(line):
                        model.setItem(model.index(rows[0]+i,columns[0]+j), cell)
            else:
                arr = [ [ cell for cell in row ] for row in reader]
                for index in selection:
                    row = index.row() - rows[0]
                    column = index.column() - columns[0]
                    model.setItem(model.index(index.row(), index.column()), arr[row][column])
        return


def keyPressEvent(self, e):
        if (e.modifiers() & QtCore.Qt.ControlModifier):
            selected = self.table.selectedRanges()
				
            if e.key() == QtCore.Qt.Key_V:#past
                first_row = selected[0].topRow()
                first_col = selected[0].leftColumn()
				
                #copied text is split by '\n' and '\t' to paste to the cells
                for r, row in enumerate(self.clip.text().split('\n')):
                    for c, text in enumerate(row.split('\t')):
                        self.tablewidget2.setItem(first_row+r, first_col+c, QTableWidgetItem(text))

            elif e.key() == QtCore.Qt.Key_C: #copy
                s = ""
                for r in xrange(selected[0].topRow(),selected[0].bottomRow()+1):
                    for c in xrange(selected[0].leftColumn(),selected[0].rightColumn()+1):
                        try:
                            s += str(self.tablewidget2.item(r,c).text()) + "\t"
                        except AttributeError:
                            s += "\t"
                        s = s[:-1] + "\n" #eliminate last '\t'
            self.clip.setText(s)
    def KeyPressEvent(self,event):
        clipboard= QApplication.clipboard()
        
        if event.matches(QKeySequence.Copy):
            print("ctrl+C")
            clipboard.setText("some text")
        if event.matches(QKeySequence.Paste):
            print("ctrl+v")
            print(clipboard.text())
        QTablewidget.KeyPressEvent(self,event)'''
        
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())

