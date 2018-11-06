# -*- coding: utf-8 -*-

"""
这个软件界面主要用于显示数据

作者： SWorker
日期： 2018.10.25
"""

import sys
import random
from PyQt5 import QtCore
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QLCDNumber)
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
        self.timer.start(3600)

        comName = QLabel(self)
        comName.setText("志晨科技")
        pe = QPalette()
        pe.setColor(QPalette.WindowText, QColor(218, 250, 233))
        comName.setPalette(pe)
        comName.setFont(QFont("微软雅黑", 30,  QFont.Bold))

        # 显示NOx信息
        nox_label = QLabel(self)
        nox_label.setText("NOx:")
        nox_pe = QPalette()
        nox_pe.setColor(QPalette.WindowText, QColor(218, 250, 233))
        nox_label.setPalette(nox_pe)
        nox_label.setFont(QFont("微软雅黑", StaticFont, QFont.Bold))

        self.show_nox2 = QLCDNumber(self)
        self.show_nox2.setStyleSheet("background-color:rgb(54, 89, 84)")
        self.show_nox2.display(12.45)

        self.show_nox = QLabel(self)
        self.show_nox.setText("1")
        self.show_nox.setFont(QFont("微软雅黑", StaticFont, QFont.Bold))

        nox_box = QHBoxLayout()
        nox_box.addStretch(1)
        nox_box.addWidget(nox_label)
        nox_box.addStretch(1)
        nox_box.addWidget(self.show_nox)
        nox_box.addStretch(3)
        nox_box.addWidget(self.show_nox2)

        # 显示PM信息
        pm_label = QLabel(self)
        pm_label.setText("PM:  ")
        pm_label.setFont(QFont("微软雅黑", StaticFont, QFont.Bold))

        self.show_pm = QLabel(self)
        self.show_pm.setText("1.1")
        self.show_pm.setFont(QFont("微软雅黑", StaticFont, QFont.Bold))

        pm_box = QHBoxLayout()
        pm_box.addStretch(1)
        pm_box.addWidget(pm_label)
        pm_box.addStretch(1)
        pm_box.addWidget(self.show_pm)
        pm_box.addStretch(3)

        # 显示GPS信息
        gps_label = QLabel(self)
        gps_label.setText("GPS:")
        gps_label.setFont(QFont("微软雅黑", StaticFont, QFont.Bold))
        
        self.show_gps = QLabel(self)
        self.show_gps.setText("123,234,345")
        self.show_gps.setFont(QFont("微软雅黑", StaticFont, QFont.Bold))

        gps_box = QHBoxLayout()
        gps_box.addStretch(1)
        gps_box.addWidget(gps_label)
        gps_box.addStretch(1)
        gps_box.addWidget(self.show_gps)
        gps_box.addStretch(1)

        # 设置好退出按钮，便于关闭程序
        quitBtn = QPushButton("sdf",self)
        #quitBtn.setIcon(QIcon("./img/bg2.png"))
        quitBtn.setIconSize(QSize(50, 50))
        quitBtn.clicked.connect(QCoreApplication.instance().quit)
        quitBtn.resize(quitBtn.sizeHint())
        quitBtn.move(50, 50)

        # 公司信息栏
        comanyMessageBox = QHBoxLayout()
        comanyMessageBox.addWidget(comName)
        comanyMessageBox.addStretch(1)
        comanyMessageBox.addWidget(quitBtn)

        # 创建布局
        vbox = QVBoxLayout()
        vbox.addLayout(comanyMessageBox)
        vbox.addStretch(1)
        vbox.addLayout(nox_box)
        vbox.addLayout(pm_box)
        vbox.addLayout(gps_box)
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
        self.setPalette(winPale)
       # self.showFullScreen()
        self.show()
    
    def onTimer(self):
        nox_number = "1." + str(random.randint(10, 99)) + "ppm"
        pm_number = "1." + str(random.randint(14, 89)) + "ug/kg"
        gps_number = str(random.randint(150, 200)) + "," +str(random.randint(260, 390)) + "," +str(random.randint(674, 790))
        self.show_nox.setText(nox_number)
        self.show_pm.setText(pm_number)
        self.show_gps.setText(gps_number)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())