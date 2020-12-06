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
        item2 = QListWidgetItem(QIcon('images/4.png'), 'Objection')
        item3 = QListWidgetItem(QIcon('images/2.png'), 'Xposed')
        item4= QListWidgetItem(QIcon("images/1.png"),'Device')
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
        self.fab2UI()
        #label1=QLabel()
        #label2=QLabel()
        layout2.addWidget(layout1)
       #layout2.addWidget(label1)
        #layout2.addWidget(label2)
        self.stack1.setLayout(layout2)
    def fab1UI(self):
        #frida的cmd命令选择
        Fridacb=QComboBox()
        Fridacb.addItem("请选择启动模式")
        Fridacb.addItem("Frida attach模式")
        Fridacb.addItem("Frida spawn模式")
        Fridacb.currentIndexChanged.connect(self.frida_mode_change)
        #frida的常见命令
        self.frida_order=QLineEdit()
        #layout_first的窗口
        layout_first_wig=QWidget()
        #os version的那个大容器
        layout_first=QHBoxLayout()
        #常见信息的展示
        os_information=QLabel()
        os_information.setText("温馨提示:编写frida的js代码请在frida-example/agent文件夹下编写，有代码提示!")
        os_information_blank=QLabel()
        #frida java层中的各级分类
        Tcb =QComboBox()
        #显示框
        self.SLabel=QTextEdit()
        #最外层的那个大容器
        layout=QVBoxLayout()
        Tcb.addItem("    请选择frida hook模版类型  ")
        Tcb.addItem("普通类方法的hook")
        Tcb.addItem("普通类方法的重载")
        Tcb.addItem("普通方法的主动调用")
        Tcb.addItem("类方法中object类型的hook")
        Tcb.addItem("类方法中自己构造数组对象")
        Tcb.addItem("类方法中对象类型强制转换")
        Tcb.addItem("frida实现java层中的接口")
        Tcb.addItem("枚举类型的hook")
        Tcb.addItem("泛型,List,Map,Set迭代打印")
        Tcb.addItem("静态字段和实例字段的hook")
        Tcb.addItem("内部类的hook,并通过反射暴力hook")
        Tcb.addItem("枚举ClassLoader,修正ClassLoader")
        layout_first.addWidget(os_information)
        layout_first.addWidget(os_information_blank)
        layout_first.addWidget(Fridacb)
        layout_first.addWidget(QLabel())
        layout_first.addWidget(Tcb)
        layout_first_wig.setLayout(layout_first)
        layout.addWidget(layout_first_wig)
        layout.addWidget(self.frida_order)
        layout.addWidget(self.SLabel)
        self.fab1.setLayout(layout)
    #frida java下选框中点击后的切换内容
    def frida_mode_change(self,i):
        if i==1:
            self.frida_order.setText("                                             USB连接:frida -U 包名 -l xxx.js           ||            无线连接非标准端口:frida -h ip -p 端口 包名 -l xxx.js")
        elif i==2:
            self.frida_order.setText("                                             USB连接:frida -UF 包名 -l xxx.js --no-pause                 ||                 无线连接非标准端口:frida -h ip -p 端口 -f 包名 -l xxx.js")
    def frida_mode_change1(self,i):
        if i==1:
            self.frida_order1.setText("                                             USB连接:frida -U 包名 -l xxx.js           ||            无线连接非标准端口:frida -h ip -p 端口 包名 -l xxx.js")
        elif i==2:
            self.frida_order1.setText("                                             USB连接:frida -UF 包名 -l xxx.js --no-pause                 ||                 无线连接非标准端口:frida -h ip -p 端口 -f 包名 -l xxx.js")

    def frida_code_change(self,i):
        print(i)
    def fab2UI(self):
        # frida的cmd命令选择
        Fridacb = QComboBox()
        Fridacb.addItem("请选择启动模式")
        Fridacb.addItem("Frida attach模式")
        Fridacb.addItem("Frida spawn模式")
        Fridacb.currentIndexChanged.connect(self.frida_mode_change1)
        # frida的常见命令
        self.frida_order1 = QLineEdit()
        # layout_first的窗口
        layout_first_wig = QWidget()
        # os version的那个大容器
        layout_first = QHBoxLayout()
        # 常见信息的展示
        os_information = QLabel()
        os_information.setText("温馨提示:编写frida的js代码请在frida-example/agent文件夹下编写，有代码提示!")
        os_information_blank = QLabel()
        # frida java层中的各级分类
        Tcb = QComboBox()
        # 显示框
        self.SLabel1 = QTextEdit()
        # 最外层的那个大容器
        layout = QVBoxLayout()
        Tcb.addItem("    请选择frida native hook模版类型  ")
        Tcb.addItem("JNI函数符号hook")
        Tcb.addItem("JNI函数参数，返回值打印和替换")
        Tcb.addItem("native层调用栈打印")
        layout_first.addWidget(os_information)
        layout_first.addWidget(os_information_blank)
        layout_first.addWidget(Fridacb)
        layout_first.addWidget(QLabel())
        layout_first.addWidget(Tcb)
        layout_first_wig.setLayout(layout_first)
        layout.addWidget(layout_first_wig)
        layout.addWidget(self.frida_order1)
        layout.addWidget(self.SLabel1)
        self.fab2.setLayout(layout)

    def tab2UI(self):
        #Xposed 还没开始学，这波估计得等到frida结束
        layout1=QVBoxLayout()
        layout2=QTabWidget()
        self.Oab1=QWidget()
        self.Oab2=QWidget()
        self.Oab3=QWidget()
        self.Oab1UI()
        self.Oab2UI()
        self.Oab3UI()
        layout2.addTab(self.Oab1,"Objection安装")
        layout2.addTab(self.Oab2,"Objection基本操作")
        layout2.addTab(self.Oab3,"Objection插件的使用")
        layout1.addWidget(layout2)
        self.stack2.setLayout(layout1)
    def Oab1UI(self):
        hlayout=QVBoxLayout()
        self.Oedit1=QTextEdit()
        hlayout.addWidget(self.Oedit1)
        self.Oab1.setLayout(hlayout)
    def Oab2UI(self):
        hlayout = QVBoxLayout()
        self.Oedit2 = QTextEdit()
        hlayout.addWidget(self.Oedit2)
        self.Oab2.setLayout(hlayout)
    def Oab3UI(self):
        hlayout = QVBoxLayout()
        self.Oedit3 = QTextEdit()
        hlayout.addWidget(self.Oedit3)
        self.Oab3.setLayout(hlayout)
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

