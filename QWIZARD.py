from PyQt5.QtWidgets import *
import sys
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        button = QPushButton("Launch")
        button.clicked.connect(self.on_button_clicked)
        layout.addWidget(button)
        sizegrip = QSizeGrip(self)
        sizegrip.setVisible(True)
    def on_button_clicked(self):
        wizardpage = QWizardPage()
        wizardpage.setTitle("wizard page")
        wizardpage.setSubTitle("subtitle")
        #wizardpage.setFinalPage(final)
        #wizardpage.setCommitPage(commit)
        #wizardpage.isComplete()
        #wizardpage.isCommitPage()
        wizardpage1 = QWizardPage()
        wizardpage1.setTitle("wizard page1")
        wizardpage1.setSubTitle("subtitle")
        wizardpage2 = QWizardPage()
        wizardpage2.setTitle("wizard page2")
        wizardpage2.setSubTitle("subtitle")
        self.wizard = QWizard()
        self.wizard.addPage(wizardpage)
        self.wizard.addPage(wizardpage1)
        self.wizard.addPage(wizardpage2)

        #self.wizard.setPage(3, wizardpage2)
        self.wizard.open()
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())