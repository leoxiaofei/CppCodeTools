import wx
from core.CctMain import *


def main():
    app = wx.App()
    frame = CCTMain(None)
    frame.Show()
    app.Bind(wx.EVT_MIDDLE_UP, frame.OnEdtHeaderMiddleUp)
    app.MainLoop()


if __name__ == '__main__':
    main()
