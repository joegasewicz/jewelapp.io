import wx


app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Jewel App")

frame.Show()


if __name__ == "__main__":
    print("loading GUI...")
    app.MainLoop()
