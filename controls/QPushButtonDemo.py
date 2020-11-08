'''
按钮控件(QPushButton)
QAbstractButton
QPushButton
AToolButton
QRadioButton
QCheckBox

'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class QPushButtonDemo(QWidget):
    def __init__(self):
        super(QPushButtonDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("QPUSHBUTTON DEMO")
        layout=QVBoxLayout()
        self.button1=QPushButton("第一个按钮")
        self.button1.setText("First Button1")
        #类似checkbox
        self.button1.setCheckable(True)
        self.button1.toggle()
        self.button1.clicked.connect(lambda:self.whichButton(self.button1))
        self.button1.clicked.connect(self.buttonState)
    def whichButton(self,btn):
        print("被淡季的按钮<"+btn.text()+">")
    def buttonState(self):
        if self.button1.isChecked():
            print("按钮1已经被选中")
        else:
            print("按钮1未被选中")
