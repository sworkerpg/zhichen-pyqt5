import wx
import time 
class MyPanel(wx.Panel):
     def __init__(self, parent):
        super(MyPanel, self).__init__(parent)



class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"My Frame",size=(400,300),
                          style = wx.DEFAULT_FRAME_STYLE)
        self.panel = wx.Panel(self)
        self.timer = wx.Timer(self)                               

        self.vBox = wx.BoxSizer(wx.VERTICAL)
        self.NOxBox = wx.BoxSizer(wx.HORIZONTAL)
        self.PMBox = wx.BoxSizer(wx.HORIZONTAL)

        self.NOxLabel = wx.StaticText(self, -1, "NOx:")
        self.NOxShow = wx.TextCtrl(self, -1, style=wx.TE_READONLY)
        self.NOxShow.SetValue("1")
        self.NOxBox.Add(self.NOxLabel, 3, wx.EXPAND, 10)
        self.NOxBox.Add(self.NOxShow, 5, wx.EXPAND, 10)
        self.vBox.Add(self.NOxBox)

        self.PMLabel = wx.StaticText(self, -1, "PM:")
        self.PMShow = wx.TextCtrl(self, -1, style=wx.TE_READONLY)
        self.PMShow.SetValue("0")
        self.PMBox.Add(self.PMLabel, 1, wx.EXPAND, 10)
        self.PMBox.Add(self.PMShow, 1, wx.EXPAND, 10)
        self.vBox.Add(self.PMBox)

        self.GPSLabel = wx.StaticText(self, -1, "GPS:")
        self.vBox.Add(self.GPSLabel, 1, wx.EXPAND, 5)

        self.SetSizer(self.vBox)
        self.panel.Bind(wx.EVT_ERASE_BACKGROUND,self.OnEraseBack)
        
    def OnEraseBack(self,event):
        dc = event.GetDC()
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("./img/bg.jpg")
        dc.DrawBitmap(bmp, 0, 0)
if __name__ == '__main__':
    app = wx.App()
    frame = Frame()
    frame.Show()
    app.MainLoop()
