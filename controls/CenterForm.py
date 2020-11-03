#QDesktopWidget

import sys
import typing

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QDockWidget,QDesktopWidget
from PyQt5.QtGui import QIcon

class CenterForm(QMainWindow):
    def __init__(self,parent=None):
        super(CenterForm, self).__init__(parent)
        #设置主窗口标题
        self.setWindowTitle("第一个窗口应用")
        #设置窗口的尺寸
        self.resize(400,300)
        #获取状态栏
        self.status=self.statusBar()

        self.status.showMessage("只存在5秒的消息",5000)
    def center(self):
        #获取屏幕坐标系
        screen=QDesktopWidget().screenGeometry()
        #获取窗口坐标系
        size=self.geometry()
        newLeft=(screen.width()-size.width())/2
        newTop=(screen.height()-size.height())/2
        self.move(newLeft,newTop)
if __name__=='__main__':
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/Dragon.ico'))
    main=CenterForm()
    main.show()
    sys.exit(app.exec_())