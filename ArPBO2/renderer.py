from typing import Text
import wx
import wx.grid

class myRenderer(wx.grid.GridCellRenderer):
    def __init__(self,img):
        wx.grid.GridCellRenderer.__init__(self)
        self.img = img

    def Draw(self,grid,attr,dc,rect,row,col,isSelected):
        image = wx.MemoryDC()
        image.SelectObject(self.img)
        dc.SetBackgroundMode(wx.SOLID)
        if isSelected:
            dc.SetBrush(wx.Brush(wx.WHITE, wx.SOLID))
            dc.SetPen(wx.Pen(wx.WHITE, 1 , wx.SOLID))
        else:
            dc.SetBrush(wx.Brush(wx.WHITE, wx.SOLID))
            dc.SetPen(wx.Pen(wx.WHITE, 1 , wx.SOLID))
        dc.DrawRectangle(rect)
        width, height = self.img.GetWidth(), self.img.GetHeight()
        if width > rect.width - 2:
            width = rect.width -2
        if height > rect.height -2:
            height = rect.height -2
        dc.Blit(rect.x + 1, rect.y + 1, width, height, image, 0,0, wx.COPY, True)
    
    def GetBestSize(self,grid,attr,dc,rect,row,col):
        text = grid.GetCellValue(row,col)
        dc.SetFont(attr.GetFont())
        w, h = dc.GetTextExtent(text)
        return wx.Size(w, h)