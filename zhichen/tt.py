import wx
 
 
 
class MyPanel(wx.Panel): 
    def __init__(self, parent, id): 
        wx.Panel.__init__(self, parent, id) 
        try: 
            image_file = './img/bg.jpg' 
            to_bmp_image = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap() 
            self.bitmap = wx.StaticBitmap(self, -1, to_bmp_image, (0, 0)) 
            image_width = to_bmp_image.GetWidth() 
            image_height = to_bmp_image.GetHeight() 
            set_title = '%s %d x %d' % (image_file, to_bmp_image.GetWidth(), to_bmp_image.GetHeight()) 
            parent.SetTitle(set_title) 
        except IOError: 
           pass
        raise SystemExit 
         #创建一个按钮 
        self.button = wx.Button(self.bitmap, -1, label='Test', pos=(10,10)) 
if __name__ == '__main__': 
    app = wx.App() 
    frame = wx.Frame(None, -1, 'Image', size=(300,300)) 
    my_panel = MyPanel(frame, -1) 
    frame.Show() 
    app.MainLoop() 
 
