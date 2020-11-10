import sys,math
from PyQt5.QtWidgets import *
class MainUi(QMainWindow):
    def __init__(self):
        super(MainUi, self).__init__()
        self.initUI()
    def initUI(self):
        self.resize(1000,800)
        self.desktopWidth=QApplication.desktop().width() #当前桌面的宽
        self.desktopHeight=QApplication.desktop().height() #当前桌面的高

        self.main_widget=QWidget() #创建窗口主部件
        self.main_widget.setObjectName("main_widget")
        self.main_layout=QGridLayout() #创建网格布局的对象
        self.main_widget.setLayout(self.main_layout)
        self.init_left()
        self.init_right()
        self.main_layout.addWidget(self.left_widget,0,0,1,1)
        self.main_layout.addWidget(self.right_widget1,0,1,1,6)
        self.main_layout.addWidget(self.right_widget2,0,1,1,6)
        self.right_widget1.hide()
        self.right_widget2.show()
        self.setCentralWidget(self.main_widget)
    def init_left(self):
        self.left_widget=QWidget() #创建左侧部件
        self.left_widget.setObjectName('left_widget') #左侧部件对象命名
        self.left_layout=QGridLayout()
        self.Button1=QPushButton("进入界面1")
        self.Button2=QPushButton("进入界面2")
        self.left_layout.addWidget(self.Button1,0,0,1,1)
        self.left_layout.addWidget(self.Button2,0,1,1,1)
        self.left_widget.setLayout(self.left_layout)

        # 把切换界面的button和两个跳转函数进行绑定
        self.Button1.clicked.connect(self.clicked_1)
        self.Button2.clicked.connect(self.clicked_2)
    def init_right(self):
        self.right_widget1=QWidget()
        self.right_layout1=QGridLayout()
        self.right_widget1.setLayout(self.right_layout1)
        self.text1=QLabel("fuck") #加一个用来界面跳转的button1
        self.text1.setText("进入界面2")
        self.right_layout1.addWidget(self.text1)

        self.right_widget2=QWidget()
        self.right_layout2=QGridLayout()
        self.right_widget2.setLayout(self.right_layout2)
        self.text2=QLabel("YenKocd")
        self.text2.setText("进入界面1")
        self.right_layout2.addWidget(self.text2)


    def clicked_1(self):
        self.right_widget1.hide()
        self.right_widget2.show()
    def clicked_2(self):
        self.right_widget2.hide()
        self.right_widget1.show()
if __name__ == '__main__':
    app=QApplication(sys.argv)
    main=MainUi()
    main.show()
    sys.exit(app.exec_())

