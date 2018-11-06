# -*- coding: utf-8 -*-

"""
这个软件界面主要用于显示数据

作者： SWorker
日期： 2018.10.25
"""

import sys
import random
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLayout, 
         QVBoxLayout, QLabel, QLCDNumber, QGridLayout, QDesktopWidget)
from PyQt5.QtGui import QIcon, QPalette, QFont, QColor
from PyQt5.QtCore import QCoreApplication, Qt, QTimer, QSize
from PyQt5 import QtGui

StaticFont = 80

class MainWindow(QWidget):
    """ 初始化界面 """
    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.initUI()

    def initUI(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.onTimer)
        self.timer.start(2000)

        self.timer1 = QTimer(self)
        self.timer1.timeout.connect(self.onTimer1)
        self.timer1.start(2115)

        grid_layout = QGridLayout()        # 创建表格布局
        grid_layout.setSpacing(10)
        vbox = QVBoxLayout()

        comName = QLabel(self)
        png = QtGui.QPixmap("./img/lg.png")
        #comName.setText("志晨科技")
        comName.setPixmap(png)
        pe = QPalette()
        pe.setColor(QPalette.WindowText, QColor(218, 250, 233))
        comName.setPalette(pe)
        comName.setFont(QFont("微软雅黑", 30,  QFont.Bold))

        # 显示NOx信息
        nox_label = QLabel(self)
        nox_label.setText("NOx:")
        
        self.show_nox = QLCDNumber(self)
        self.show_nox.display(12.5)

        nox_msg = QLabel(self)
        nox_msg.setText("ppm")

        # 显示pm信息
        pm_label = QLabel(self)
        pm_label.setText("PM:  ")

        self.show_pm = QLCDNumber(self)
        self.show_pm.display(1.20)

        pm_msg = QLabel(self)
        pm_msg.setText("ug/kg")
        
        # 显示gps信息
        gps_label = QLabel(self)
        gps_label.setText("GPS:")

        #self.show_gps = QLCDNumber(self)
        #self.show_gps.display(123.456)
        self.show_gps = QLabel(self)
        self.show_gps.setText("123,456,789")

        grid_layout.addWidget(nox_label, 1, 0)
        grid_layout.addWidget(self.show_nox, 1, 1, 1, 5)
        grid_layout.addWidget(nox_msg, 1, 6)

        grid_layout.addWidget(pm_label, 2, 0)
        grid_layout.addWidget(self.show_pm, 2, 1,1, 5)
        grid_layout.addWidget(pm_msg, 2, 6)

        grid_layout.addWidget(gps_label, 3, 0)
        grid_layout.addWidget(self.show_gps, 3, 1)

        vbox.addWidget(comName)
        vbox.addStretch(1)
        vbox.addLayout(grid_layout)
        vbox.addStretch(1)

        self.setLayout(vbox)

        # 导入样式表
        with open('./stylesheet/stylesheet.txt') as file:
            str = file.readlines()
            str = ''.join(str).strip('\n')
        self.setStyleSheet(str)

        self.setWindowTitle("志晨科技")
        # 设置背景图片
        winPale = QtGui.QPalette()
        #winPale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("./img/bg.jpg")))
        winPale.setColor(self.backgroundRole(), QColor(199, 206, 209))
        self.setWindowIcon(QIcon("./img/logo.png"))
        self.setPalette(winPale)
        self.resize(623, 332)
        self.center()
       # self.showFulScreen()
        self.show()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
        (screen.height() - size.height())/2 )
    
    def onTimer(self):
        nox_number = round(random.uniform(1.5, 2.5), 2)
        self.show_nox.display(nox_number)
        gps_number = str(random.randint(186, 205)) + "," +str(random.randint(363, 389)) + "," +str(random.randint(674, 692))
        self.show_gps.setText(gps_number)

    def onTimer1(self):
        pm_number = round(random.uniform(1.6, 2.4), 2)
        self.show_pm.display(pm_number)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())