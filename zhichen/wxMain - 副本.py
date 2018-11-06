# -*- coding: utf-8 -*-

"""
这个软件界面主要用于显示数据

作者： SWorker
日期： 2018.10.30
"""

import wx
import time
import random

class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)
        font = wx.Font(150, wx.DECORATIVE, wx.SLANT, wx.FONTWEIGHT_BOLD)

        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBack)


        self.timer = wx.Timer(self)                                         # 创建定时器
        self.Bind(wx.EVT_TIMER, self.OnTimer, self.timer)     # 绑定一个定时器事件
        self.timer.Start(500)                                                   # 设定时间间隔

        self.vBox = wx.BoxSizer(wx.VERTICAL)
        self.NOxBox = wx.BoxSizer(wx.HORIZONTAL)
        self.PMBox = wx.BoxSizer(wx.HORIZONTAL)

        self.NOxLabel = wx.StaticText(self, -1, "NOx: ")
        self.NOxLabel.SetFont(font)
        self.NOxShow = wx.TextCtrl(self, -1, style=wx.TE_READONLY)
        self.NOxShow.SetValue("1")
        self.NOxBox.Add(self.NOxLabel)
        self.NOxBox.Add(self.NOxShow)
        self.vBox.Add(self.NOxBox)

        self.PMLabel = wx.StaticText(self, -1, "PM:  ")
        self.PMLabel.SetFont(font)
        self.PMShow = wx.TextCtrl(self, -1, style=wx.TE_READONLY)
        self.PMShow.SetValue("0")
        self.PMBox.Add(self.PMLabel)
        self.PMBox.Add(self.PMShow)
        self.vBox.Add(self.PMBox)

        self.GPSLabel = wx.StaticText(self, -1, "GPS:")
        self.GPSLabel.SetFont(font)
        self.vBox.Add(self.GPSLabel)

        self.SetSizer(self.vBox)

    def OnTimer(self, evt):
        self.NOxShow.SetValue(str(random.randint(0,9)/10.0 +1))
        self.PMShow.SetValue(str(random.randint(1,8)/10.0 +1))

    def OnEraseBack(self, event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRegion(rect)
        dc.Clear()
        bmp = wx.Bitmap("./img/bg.jpg")
        dc.DrawBitmap(bmp, 0, 0)
class MyFrame(wx.Frame):
    def __init__(self, parent, title=""):
        super(MyFrame, self).__init__(parent, title=title)

        self.SetIcon(wx.Icon("./img/logo.png"))


        self.panel = MyPanel(self)

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None, title = "")
        self.frame.Show()
        #wx.MessageBox("Hello wxPython", "wxAPP")
        return True
    
if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()