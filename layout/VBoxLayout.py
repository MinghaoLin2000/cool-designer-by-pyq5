'''
垂直布局
'''

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
class VBoxLayout(QWidget):
    def __init__(self):
        super(VBoxLayout, self).__init__()
        self.setWindowTitle("水平盒布局")

        vlayout=QVBoxLayout()
        vlayout.addWidget(QPushButton("按钮1"),1,Qt.AlignLeft | Qt.AlignTop)
        vlayout.addWidget(QPushButton("按钮2"),1,Qt.AlignLeft | Qt.AlignTop)
        vlayout.addWidget(QPushButton("按钮3"),1,Qt.AlignLeft | Qt.AlignTop)
        vlayout.addWidget(QPushButton("按钮4"),1,Qt.AlignLeft | Qt.AlignTop)
        vlayout.addWidget(QPushButton("按钮5"),1,Qt.AlignLeft | Qt.AlignTop)
        vlayout.setSpacing(40) #间距
        self.setLayout(vlayout)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    main=VBoxLayout()
    main.show()
    sys.exit(app.exec_())