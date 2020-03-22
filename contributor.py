from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QLabel

class Contributor(QWidget):
    def __init__(self, index, data_item):
        super().__init__()
        
        uic.loadUi("contributor.ui", self)
        
        self.rank.setText("#%d" % (index+1))
        
        self.name.setText(data_item['username'])
        self.subtext.setText("%d PRs opened" % data_item['count'])
    
