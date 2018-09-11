#coding:utf-8
import wx
class Frame1(wx.Frame):
    def __init__(self,superior):
        wx.Frame.__init__(self,parent=superior,title="Hello World")
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.text1 = wx.TextCtrl(panel,value="Text",size=(200,180),style=wx.TE_MULTILINE)
        sizer.Add(self.text1,0,wx.ALIGN_TOP|wx.EXPAND)
        button = wx.Button(panel,label="Click Me")
        sizer.Add(button)
        panel.SetSizerAndFit(sizer)
        panel.Layout()
        self.Bind(wx.EVT_BUTTON,self.OnClick,button)
    def OnClick(self,text):
        self.text1.AppendText("\nHello,World!")
        pass
    
frame = Frame1(wx.Frame)
