import sys

from PyQt5.QtCore import QRect, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *


class MainUi(QWidget):
    def __init__(self):
        super(MainUi, self).__init__()
        self.setObjectName('MainWindow')
        self.setStyleSheet('#MainWindow{border-image:url(images/1.jpg);}')
        self.initUI()
    #采用堆栈窗口控件
    def initUI(self):
        self.resize(1500,800)
        self.setWindowTitle("Android killer growing")
        #列表控件，列举出主要hook的东西
        self.list=QListWidget()
        self.list.setStyleSheet("QListWidget{border:1px solid gray; color:black; }"
                           "QListWidget::Item{padding-top:20px; padding-bottom:4px; }"
                           "QListWidget::Item:hover{background:skyblue; }"
                           "QListWidget::item:selected{background:lightgray; color:white; }"
                           "QListWidget::item:selected:!active{border-width:0px; background:lightgreen; }"
                           )
        item1 = QListWidgetItem(QIcon('images/3.png'), 'Frida')
        item2 = QListWidgetItem(QIcon('images/1.png'), 'Xposed')
        item3 = QListWidgetItem(QIcon('images/2.png'), 'Device')
        self.list.setIconSize(QSize(100,100))
        self.list.insertItem(0,item1)
        self.list.insertItem(1,item2)
        self.list.insertItem(2,item3)

        self.stack1=QWidget()
        self.stack2=QWidget()
        self.stack3=QWidget()
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()

        self.stack=QStackedWidget()
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)
        hbox=QHBoxLayout()
        hbox.addWidget(self.list,1)
        hbox.addWidget(self.stack,3)
        self.setLayout(hbox)

        self.list.currentRowChanged.connect(self.display)
    def display(self,index):
        self.stack.setCurrentIndex(index)
    def tab1UI(self):
        #java层和native层的按钮，水平布局
        layout2=QVBoxLayout()
        layout1=QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        layout1.addTab(self.tab1,"frida java script")
        layout1.addTab(self.tab2,"frida native script")
        label1=QLabel()
        label2=QLabel()
        layout2.addWidget(layout1)
        layout2.addWidget(label1)
        layout2.addWidget(label2)
        self.stack1.setLayout(layout2)
    def tab2UI(self):
        #Xposed 还没开始学，这波估计得等到frida结束
        layout2=QVBoxLayout()
        label2=QLabel("未完待续")
        self.stack2.setLayout(layout2)
    def tab3UI(self):
        #device 这里adb搞定一切问题
        layout2=QVBoxLayout()
        label2=QLabel("未完待续")
        self.stack3.setLayout(layout2)

    '''def initUI(self):
        self.resize(1500,800)
        self.desktopWidth=QApplication.desktop().width() #当前桌面的宽
        self.desktopHeight=QApplication.desktop().height() #当前桌面的高
        self.main_widget=QWidget() #创建窗口主部件
        self.main_widget.setObjectName("main_widget")
        self.main_layout=QGridLayout() #创建网格布局的对象
        self.main_widget.setLayout(self.main_layout)
        self.init_left()
        self.init_right()
        #self.left_widget.setStyleSheet('background-color:qlineargradient(x1:0, y1:0, x2:1, y2:1,stop:0 red,stop:0.4 gray,stop:0.8 orange,stop:1 green);')
        self.main_layout.addWidget(self.left_widget,0,0,1,1)
        self.main_layout.addWidget(self.right_widget1,0,1,-1,3)
        self.main_layout.addWidget(self.right_widget2,0,1,-1,3)
        self.right_widget1.hide()
        self.right_widget2.show()
        self.setCentralWidget(self.main_widget)
    def init_left(self):
        self.left_widget=QWidget() #创建左侧部件
        self.left_widget.setObjectName('left_widget') #左侧部件对象命名
        self.left_layout=QVBoxLayout()
        self.Button1=QPushButton("Frida")
        self.Button2=QPushButton("Xposed")
        self.Button3 = QPushButton("Device")
        self.Button4 = QPushButton("Poc")
        self.left_layout.addWidget(self.Button1)
        self.left_layout.addWidget(self.Button2)

        self.left_layout.addWidget(self.Button3)

        self.left_layout.addWidget(self.Button4)

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
    '''
    #显示一波小组件
    '''def clicked_3(self):
        self.Button5.show()
        self.Button6.show()'''
if __name__ == '__main__':
    app=QApplication(sys.argv)
    main=MainUi()
    main.show()
    sys.exit(app.exec_())

