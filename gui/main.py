import wx

from app.open_gl_frame import OpenGLFrame


if __name__ == "__main__":
    print("loading GUI...")
    app = wx.App(False)
    frame = OpenGLFrame()
    frame.Show()
    app.MainLoop()
