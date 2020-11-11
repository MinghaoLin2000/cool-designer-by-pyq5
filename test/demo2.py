#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PyQt5 教程

这个例子说明如何使用QSplitter部件。

作者：我的世界你曾经来过
博客：http://blog.csdn.net/weiaitaowang
最后编辑：2016年8月4日
"""

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout,
QFrame, QSplitter)
from PyQt5.QtCore import Qt

class Example(QWidget):

  def __init__(self):
    super().__init__()

    self.initUI()

  def initUI(self):

    hbox = QHBoxLayout(self)

    topleft = QFrame(self)
    topleft.setFrameShape(QFrame.StyledPanel)

    topright = QFrame(self)
    topright.setFrameShape(QFrame.StyledPanel)

    bottom = QFrame(self)
    bottom.setFrameShape(QFrame.StyledPanel)

    splitter1 = QSplitter(Qt.Horizontal)
    splitter1.addWidget(topleft)
    splitter1.addWidget(topright)

    splitter2 = QSplitter(Qt.Vertical)
    splitter2.addWidget(splitter1)
    splitter2.addWidget(bottom)

    hbox.addWidget(splitter2)
    self.setLayout(hbox)

    self.setGeometry(300, 300, 300, 200)
    self.setWindowTitle('窗口分隔')
    self.show()

if __name__ == '__main__':

  app = QApplication(sys.argv)
  ex = Example()
  sys.exit(app.exec_())

