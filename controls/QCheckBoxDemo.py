'''
复选框控件(QCheckBox)
微选中：0
半选中：1
选中：2
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
class QCheckBoxDemo(QWidget):
    def __init__(self):
        super(QCheckBoxDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("复选框控件演示")
        layout=QHBoxLayout()
        self.checkBox1=QCheckBox('复选框控件1')
        self.checkBox1.setChecked(True)
        self.checkBox2 = QCheckBox('复选框控件2')
        self.checkBox2.setChecked(True)
        self.checkBox3 = QCheckBox('复选框控件3')
        self.checkBox3.setChecked(True)
        self.checkBox1.stateChanged.connect(lambda :self.checkboxState(self.checkBox1))
        self.checkBox2.stateChanged.connect(lambda: self.checkboxState(self.checkBox2))
        self.checkBox3.stateChanged.connect(lambda: self.checkboxState(self.checkBox3))
    def checkboxState(self,cb):
        checkState1=self.checkBox1.text()+", ischecked="+str(self.checkBox1.isChecked())+',checkState'+ str(self.checkBox1.checkState())
        checkState2=self.checkBox2.text()+", ischecked="+str(self.checkBox2.isChecked())+',checkState'+ str(self.checkBox2.checkState())
        checkState3=self.checkBox3.text()+", ischecked="+str(self.checkBox3.isChecked())+',checkState'+ str(self.checkBox3.checkState())
        print(checkState1+checkState2+checkState3)
