'''
QLabel

setAlignment():设置文本对齐
setIndent():设置文本缩紧
text():设置文本内容
setBuddy():设置伙伴关系
selectedText():返回所选择的字符
setWordWrap():设置是否允许换行

QLabel常用的信号(事件)
1. 当鼠标滑过QLabel控件时触发: linkHovered
2. 当鼠标单击QLabel控件时触发: linkActivated


'''
import sys
import typing
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget,QHBoxLayout,QPushButton,QLabel,QVBoxLayout
from PyQt5.QtGui import QPalette,QPixmap
from PyQt5.QtCore import Qt
class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        label1=QLabel(self)
        label2=QLabel(self)
        label3=QLabel(self)
        label4=QLabel(self)
        label1.setText("<font color=yellow>这是一个文本标签.</font>")
        label1.setAutoFillBackground(True)
        patette=QPalette()
        patette.setColor(QPalette.Window,Qt.blue)
        label1.setPalette(patette)
        label1.setAlignment(Qt.AlignCenter)
        label2.setText("<a href='#>欢迎使用Python GUI程序</a>")
        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip("这是一个图片标签")
        label3.setPixmap(QPixmap("./images/python.jpg"))
        label4.setText("<a href='https://item.jd.com'>感谢关注</a>")
        label4.setOpenExternalLinks(True)
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip("这是一个超级链接")
        vbox=QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)
        self.setLayout(vbox)
        self.setWindowTitle("qlabel控件演示")
    def linkHovered(self):
        print("当鼠标滑过label2标签")
    def linkClicked(self):
        print("当鼠标单击label4标签")
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QLabelDemo()
    main.show()
    sys.exit(app.exec_())