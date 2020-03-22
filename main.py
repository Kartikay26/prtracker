import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

from data_source import fetch_data
from contributor import Contributor

COLS = 3

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Load the UI Page
        uic.loadUi('mainwin.ui', self)

        self.actionOpen.triggered.connect(self.openFile)
        self.actionSave.triggered.connect(self.saveFile)
        self.fetchbtn.clicked.connect(self.fetch)
        self.hideselectedbtn.clicked.connect(self.hideSelected)
        self.showhiddenbtn.toggled.connect(self.toggleHidden)
        self.timerange.activated.connect(self.selectTimeRange)

        self.data = []
        self.max_days = 1
    
    def openFile(self):
        print("open file")
    
    def saveFile(self):
        print("save file")
    
    def fetch(self):
        self.statusBar().showMessage("Fetching data, please wait... ")
        self.data = fetch_data(self.repourl.text(), self.max_days)  
        self.statusBar().showMessage("Done fetching data.", 2500)

        self.refreshData()
    
    def toggleHidden(self, state):
        print("toggle", state)

    def selectTimeRange(self, x):
        self.max_days = [1, 3, 7, 30, 2*30, 3*30, 6*30][x]

    def hideSelected(self):
        print("hide")
    
    def refreshData(self):
        for i, data_item in enumerate(self.data):
            item = Contributor(i, data_item)
            self.contributors.addWidget(item, i // COLS, i % COLS)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    app.exec_()
