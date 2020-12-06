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
        self.layoutLeft=QVBoxLayout()
        self.cb=QComboBox()
             #单个添加条目
        self.cb.addItem('C')
        self.cb.addItem('C++')
        self.cb.addItem('Python')
             #多个添加条目
        self.cb.addItems(['Java','C#','PHP'])
             #当下拉索引发生改变时发射信号触发绑定的事件
        #self.cb.currentIndexChanged.connect(self.selectionchange)
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
        item4= QListWidgetItem(QIcon("images/4.png"),'Objection')
        self.list.setIconSize(QSize(100,100))
        self.list.insertItem(0,item1)
        self.list.insertItem(1,item2)
        self.list.insertItem(2,item3)
        self.list.insertItem(3,item4)

        self.stack1=QWidget()
        self.stack2=QWidget()
        self.stack3=QWidget()
        self.stack4=QWidget()
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.tab4UI()

        self.stack=QStackedWidget()
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)
        self.stack.addWidget(self.stack4)
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
        self.fab1 = QWidget()
        self.fab2 = QWidget()
        self.fab3 = QWidget()
        layout1.addTab(self.fab1,"frida java script")
        layout1.addTab(self.fab2,"frida native script")
        self.fab1UI()
        #label1=QLabel()
        #label2=QLabel()
        layout2.addWidget(layout1)
       #layout2.addWidget(label1)
        #layout2.addWidget(label2)
        self.stack1.setLayout(layout2)
    def fab1UI(self):
        #layout_first的窗口
        layout_first_wig=QWidget()
        #os version的那个大容器
        layout_first=QHBoxLayout()
        #常见信息的展示
        os_information=QLabel()
        os_information.setText("os_version:")
        os_information_blank=QLabel()
        phone_name=QLabel()
        phone_name.setText("Phone_name")
        phone_name_blank=QLabel()
        #frida java层中的各级分类
        Tcb =QComboBox()
        #显示框
        SLabel=QTextEdit()
        #最外层的那个大容器
        layout=QVBoxLayout()
        Tcb.addItem("普通hook")
        Tcb.addItem("")
        layout_first.addWidget(os_information)
        layout_first.addWidget(os_information_blank)
        layout_first.addWidget(phone_name)
        layout_first.addWidget(phone_name_blank)
        layout_first.addWidget(Tcb)

        layout_first_wig.setLayout(layout_first)
        layout.addWidget(layout_first_wig)
        layout.addWidget(SLabel)
        self.fab1.setLayout(layout)
    #frida java下选框中点击后的切换内容

    def tab2UI(self):
        #Xposed 还没开始学，这波估计得等到frida结束
        layout2=QVBoxLayout()
        label2=QLabel("未完待续")
        layout2.addWidget(label2)
        self.stack2.setLayout(layout2)
    def tab3UI(self):
        #device 这里adb搞定一切问题
        layout2=QVBoxLayout()
        label2=QLabel("未完待续")
        layout2.addWidget(label2)
        self.stack3.setLayout(layout2)
    def tab4UI(self):
        layout4=QVBoxLayout()
        label4=QLabel("未完待续呀")
        layout4.addWidget(label4)
        self.stack4.setLayout(layout4)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    main=MainUi()
    main.show()
    sys.exit(app.exec_())

