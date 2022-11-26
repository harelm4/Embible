from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
class Window(QMainWindow):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super(Window,self).__init__()
        self.setGeometry(100,100,1600,800)
        self.initUI()
    def initUI(self):
        self.lable=QtWidgets.QLabel(self)
        self.lable.setText('hello')
        self.lable.move(10,10)
    def showWin(self):
        self.show()
        sys.exit(self.app.exec_())

