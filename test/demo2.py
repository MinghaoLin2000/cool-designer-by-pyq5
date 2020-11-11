#QListWidget 控件使用
from PyQt5.QtWidgets import   QMessageBox,QListWidget,QListWidgetItem, QStatusBar,  QMenuBar,QMenu,QAction,QLineEdit,QStyle,QFormLayout,   QVBoxLayout,QWidget,QApplication ,QHBoxLayout, QPushButton,QMainWindow,QGridLayout,QLabel
from PyQt5.QtGui import QIcon,QPixmap,QStandardItem,QStandardItemModel,QCursor
from PyQt5.QtCore import QStringListModel,QAbstractListModel,QModelIndex,QSize,Qt
import sys

class WindowClass(QWidget):

    def __init__(self,parent=None):
        self.f=""
        super(WindowClass, self).__init__(parent)
        self.layout=QVBoxLayout()
        self.resize(400,300)
        self.view=QListWidget()
        #self.view.setViewMode(QListWidget.ListMode) #QListWidget.IconMode

        self.view.setLineWidth(50)
        self.view.addItems(["C","A","D","S"])
        self.layout.addWidget(self.view)
        self.setLayout(self.layout)

        self.view.clicked.connect(self.check)#单击选中某一个选项
        '''''
            创建右键菜单
            '''
        # 必须将ContextMenuPolicy设置为Qt.CustomContextMenu
        # 否则无法使用customContextMenuRequested信号
        self.setContextMenuPolicy(Qt.CustomContextMenu)


        # 创建QMenu
        self.contextMenu = QMenu(self)
        self.actionA = self.contextMenu.addAction(QIcon("images/0.png"), u'|  删除')

        # 显示菜单
        self.customContextMenuRequested.connect(self.showContextMenu)

        #点击删除menu
        self.contextMenu.triggered[QAction].connect(self.remove)

    def check(self,index):
        r=index.row()
        self.f=r;
    def showContextMenu(self):
        #如果有选中项，则显示显示菜单
        items=self.view.selectedIndexes()
        if items:
          self.contextMenu.show()
          self.contextMenu.exec_(QCursor.pos())  # 在鼠标位置显示
    def remove(self,qAction):
        print(self.f)
        #self.view.takeItem(self.f)#删除行(实际上是断开了与list的联系)

        #注意：removeItemWidget(self, QListWidgetItem)  # 移除一个Item，无返回值
        #注意：takeItem(self, int)  # 切断一个Item与List的联系，返回该Item
        self.view.removeItemWidget(self.view.takeItem(self.f))  #删除

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=WindowClass()
    win.show()
    sys.exit(app.exec_())