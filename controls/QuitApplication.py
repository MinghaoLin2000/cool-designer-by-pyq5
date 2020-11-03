import sys
import typing
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget,QHBoxLayout,QPushButton
from PyQt5.QtGui import QIcon
class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication,self).__init__()
        self.resize(300,120)
        self.setWindowTitle("退出应用程序")
        #添加button
        self.button1=QPushButton("退出应用程序")
        #关联

        self.button1.clicked.connect(self.onClick_Button)
        layout=QHBoxLayout()
        #加组件
        layout.addWidget(self.button1)
        mainFrame=QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def onClick_Button(self):
        sender=self.sender()
        print(sender.text()+"被按下")
        app=QApplication.instance()
        #退出应用程序
        app.quit()
if __name__ == '__main__':
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/Dragon.ico'))
    main=QuitApplication()
    main.show()
    sys.exit(app.exec_())
