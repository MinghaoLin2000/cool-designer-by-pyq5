import sys
import loginUI
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = loginUI.Ui_login_Ui()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())