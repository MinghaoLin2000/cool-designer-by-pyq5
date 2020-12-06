#login.py

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: jyroy
import sys

from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit
from qtpy import QtGui
import pymysql
import demo1

from Header import TitleBar,FramelessWindow

StyleSheet = """
/*最小化最大化关闭按钮通用默认背景*/
#buttonMinimum,#buttonMaximum,#buttonClose {
    border: none;
}
/*悬停*/
#buttonMinimum:hover,#buttonMaximum:hover {

    color: white;
}
#buttonClose:hover {
    color: white;
}
/*鼠标按下不放*/
#buttonMinimum:pressed,#buttonMaximum:pressed {

}
#buttonClose:pressed {
    color: white;

}
"""   #标题栏Button的样式

StyleSheet_2 = """
QComboBox{
        height: 20px;
        border-radius: 4px;
        border: 1px solid rgb(111, 156, 207);
        background: white;
}
QComboBox:enabled{
        color: grey;
}
QComboBox:!enabled {
        color: rgb(80, 80, 80);
}
QComboBox:enabled:hover, QComboBox:enabled:focus {
        color: rgb(51, 51, 51);
}
QComboBox::drop-down {
        background: transparent;
}
QComboBox::drop-down:hover {
        background: lightgrey;
}

QComboBox QAbstractItemView {
        border: 1px solid rgb(111, 156, 207);
        background: white;
        outline: none;
}

 QLineEdit {
        border-radius: 4px;
        height: 20px;
        border: 1px solid rgb(111, 156, 207);
        background: white;
}
QLineEdit:enabled {
        color: rgb(84, 84, 84);
}
QLineEdit:enabled:hover, QLineEdit:enabled:focus {
        color: rgb(51, 51, 51);
}
QLineEdit:!enabled {
        color: rgb(80, 80, 80);
}


"""   #QComobox和QLineEdite的样式

StyleSheet_btn = """
QPushButton{
    height:30px;
    background-color: transparent;
    color: grey;
    border: 2px solid #555555;
    border-radius: 6px;

}
QPushButton:hover {
    background-color: white;
    border-radius: 6px;

}
"""  #登录Button的样式

class loginWnd(QWidget):
    '''登录窗口'''
    def __init__(self, *args, **kwargs):
        super(loginWnd, self).__init__()
        self._layout = QVBoxLayout(spacing=0)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self.setAutoFillBackground(True)

        #self.setWindowOpacity(0.1)
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("images/2.jpg")))
        self.setPalette(window_pale)

        self.setLayout(self._layout)
        self._setup_ui()

    def _setup_ui(self):

        self.main_layout = QGridLayout()

        self.main_layout.setAlignment(Qt.AlignCenter)

        self.name_label = QLabel('用户名:')
        self.name_label.setStyleSheet("color:white;")
        self.passwd_label = QLabel('密码:')
        self.passwd_label.setStyleSheet("color:white;")

        self.name_box = QLineEdit()
        #name_box.setEditable(True)
        self.passwd_box = QLineEdit()
        self.passwd_box.setEchoMode(QLineEdit.Password)
        self.name_box.setStyleSheet(StyleSheet_2)
        self.passwd_box.setStyleSheet(StyleSheet_2)

        self.label = QLabel()

        self.login_btn = QPushButton("登录")
        self.login_btn.setStyleSheet("color:white;")
        self.login_btn.setStyleSheet(StyleSheet_btn)
        self.login_btn.clicked.connect(self.login_Judge)
        self.register_btn=QPushButton("注册")
        self.register_btn.setStyleSheet(StyleSheet_btn)
        self.main_layout.addWidget(self.name_label,0,0,1,1)
        self.main_layout.addWidget(self.passwd_label,1,0,1,1)
        self.main_layout.addWidget(self.name_box,0,1,1,2)
        self.main_layout.addWidget(self.passwd_box,1,1,1,2)
        self.main_layout.addWidget(self.label,3,0,1,3)
        self.main_layout.addWidget(self.login_btn,4,0,1,2)
        self.main_layout.addWidget(self.register_btn,4,2,1,2)

        self._layout.addLayout(self.main_layout)
    #登陆
    def login_Judge(self):
        username=self.name_box.text()
        password=self.passwd_box.text()
        #这里mysql先安排一手，直接从数据进行一波判断
        if username=='':
            OK = QMessageBox.warning(self, ("警告"), ("""请输入账号！"""))
        if password=='':
            OK = QMessageBox.warning(self, ("警告"), ("""请输入密码！"""))
        if username =='admin' and password=='123':
            self.newMain=demo1.MainUi()
            self.newMain.show()
            self.close()
        else:
            OK = QMessageBox.warning(self, ("警告"), ("""用户名或密码不正确！"""))

    #注册(这里得用数据库来弄)

'''def main():

    app = QApplication(sys.argv)

    mainWnd = FramelessWindow()
    mainWnd.setWindowTitle('Android hook')
    mainWnd.setWindowIcon(QIcon('Qt.ico'))  #因为这里固定了大小，所以窗口的大小没有办法任意调整，想要使resizeWidget函数生效的话要把这里去掉，自己调节布局和窗口大小
    mainWnd.setWidget(loginWnd(mainWnd))  # 把自己的窗口添加进来
    mainWnd.show()

    app.exec()
'''
if __name__ == '__main__':
    app=QApplication(sys.argv)
    mainWnd=loginWnd()
    mainWnd.setWindowTitle("Android hook")
    mainWnd.resize(1000,500)
    #mainWnd.setObjectName("MainWindow")
    #mainWnd.setStyleSheet("#MainWindow{border-image:url(images/2.jpg)}")
    mainWnd.show()
    app.exec_()