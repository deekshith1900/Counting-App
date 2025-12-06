import wx
app=wx.App()

class countapp(wx.Frame):
    def __init__(self):
        super().__init__(None,title="Counting App",size=(400,400))
        
        self.panel=wx.Panel(self)
        self.panel.SetBackgroundColour("grey")
        
        self.btn=wx.Button(self.panel,label="Lets start the match!",pos=(130,30))
        self.btn.Bind(wx.EVT_BUTTON,self.start)
        
    
        
        self.text=wx.StaticText(self.panel,label="round count :0",pos=(150,100))

        self.btn1=wx.Button(self.panel,label="next round",pos=(150,200))
        self.btn1.Disable()
        self.btn2=wx.Button(self.panel,label="End Game !",pos=(150,250))
        self.btn2.Disable()
        self.btn3=wx.Button(self.panel,label="restart game !",pos=(150,300))
        self.btn3.Disable()
        self.btn1.Bind(wx.EVT_BUTTON,self.increase)
        self.btn2.Bind(wx.EVT_BUTTON,self.over)
        self.btn3.Bind(wx.EVT_BUTTON,self.restart)
    def start(self,event):
        self.btn.SetLabel("Match Started!!")
        self.count=0
        self.btn1.Enable()
        self.btn2.Enable()
        self.btn3.Disable()

    def increase(self,event):
        self.count+=1
        self.text.SetLabel(f"round count:{self.count}")

    def over(self,event):
        dlg=wx.MessageDialog(self,f"Game Over! with {self.count} rounds","Game Result",wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        
        self.btn1.Disable()
        self.btn2.Disable()
        self.btn3.Enable()
    def restart(self,event):
        self.count=0
        self.text.SetLabel("round count:0")

        self.btn.Enable()
        self.btn3.Disable()
        self.btn2.Disable()
        self.btn1.Disable()

        self.btn.SetLabel("New Game")

frame=countapp()
frame.Show()
app.MainLoop()

