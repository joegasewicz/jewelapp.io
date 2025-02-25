import wx
from app.canvas import JewelCanvas


class OpenGLFrame(wx.Frame):

    def __init__(self):
        super().__init__(None, title="Jewel App", size=(960, 720))
        canvas = JewelCanvas(self)
