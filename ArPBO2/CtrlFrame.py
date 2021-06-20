import wx 
from Wx192083 import *
from DB import GO
import renderer
class App(wx.App):
    appFrame = None

    def OnInit(self):
        self.appFrame = CtrlFrame_Login(Frame_Login(None))
        self.appFrame.Show()
        return True
        
###########################################################################
## Class Frame_Login
###########################################################################



class CtrlFrame_Login(Frame_Login):
    def onloginuser(self,event):
        query = "SELECT * FROM admin"
        tes = GO()
        data_login = tes.get(query)
        count = 0
        for i in data_login:
            if self.input_username.GetValue() == i[0] and self.input_password.GetValue() == i[1]:
                print("berhasil login")
                self.appFrame = Ctrldialog_loginberhasil(dialog_loginberhasil(None))
                self.appFrame.Show()
                self.Hide()
                count += 1
        
        if count == 0:
            print("gagal login")
            self.appFrame = Ctrldialog_logingagal(dialog_logingagal(None))
            self.appFrame.Show()


############################# Dialog Frame_Login ##########################

class Ctrldialog_loginberhasil(dialog_loginberhasil):
    def onloginberhasil(self,event):
        self.appFrame = CtrlFrame_Pesan(Frame_Pesan(None))
        self.appFrame.Show()
        self.Destroy()


class Ctrldialog_logingagal(dialog_logingagal):
    def onlogingagal(self,event):
        event.Skip()







###########################################################################
## Class Frame_Pesan
###########################################################################


class CtrlFrame_Pesan(Frame_Pesan):
    def __init__(self,parent):
        Frame_Pesan.__init__(self,parent=None)
        print('Frame Pemesanan')

    def onmenuPesanan(self,event):
        self.appFrame = CtrlFrame_Data(Frame_Data(None))
        self.appFrame.Show()
        self.Destroy()
    
    def onPesan(self,event):
        kodelap = self.input_code.GetValue()
        Waktu = self.waktu_awal.GetValue() + ' - ' + self.waktu_akhir.GetValue()
        Nama = self.input_nama.GetValue()
        Tim = self.input_tim.GetValue()
        Tanggal = str(self.tanggal.GetValue()) + '' + self.bulan.GetValue() + ' ' + str(self.tahun.GetValue())
        NoHP = self.input_nohp.GetValue()

        val = (kodelap,Waktu,Nama,Tim,Tanggal,NoHP)
        tes  = GO()
        tambahkan = tes.Insert_Grid(val)
        print('Pesanan Ditambahkan')

        self.appFrame = Ctrldialog_pesan(dialog_pesan(None))
        self.appFrame.Show()


    def onHapus(self,event):
        self.appFrame = Ctrldialog_hapus(dialog_hapus(None))
        self.appFrame.Show()

    
############################# Dialog Frame_Pesan ###########################

class Ctrldialog_pesan(dialog_pesan):
    
    def ondialog_pesan(self,event):
        event.Skip()

class Ctrldialog_hapus(dialog_hapus):

    def ondialog_hapus(self,event):
        event.Skip()

    def ondialog_cancel(self,event):
        event.Skip()








###########################################################################
## Class Frame_Data
###########################################################################

class CtrlFrame_Data(Frame_Data):
    def __init__(self,parent):
        Frame_Data.__init__(self,parent=None)
        self.view_lap1()
        self.view_lap2()
        self.view_lap3()
        self.addEditDelete()
        
    
    def addEditDelete(self):
        imgEDT = wx.Bitmap("EDT.PNG",wx.BITMAP_TYPE_PNG)
        imgDLT = wx.Bitmap("DLT.PNG",wx.BITMAP_TYPE_PNG)
        colEDT = 6
        colDLT = 7
        self.rdEDT = renderer.myRenderer(imgEDT)
        self.rdDLT = renderer.myRenderer(imgDLT)
        for row in range (self.grid_lap1.GetNumberRows()):
            self.grid_lap1.SetCellRenderer(row, colEDT, self.rdEDT)
            self.grid_lap1.SetCellRenderer(row, colDLT, self.rdDLT)

        for row in range (self.grid_lap2.GetNumberRows()):
            self.grid_lap2.SetCellRenderer(row, colEDT, self.rdEDT)
            self.grid_lap2.SetCellRenderer(row, colDLT, self.rdDLT)

        for row in range (self.grid_lap3.GetNumberRows()):
            self.grid_lap3.SetCellRenderer(row, colEDT, self.rdEDT)
            self.grid_lap3.SetCellRenderer(row, colDLT, self.rdDLT)

    
    
    def view_lap1(self):
        kolom = ['Kode Lap','Waktu','Nama','Tim','Tanggal','NoHP']
        query = "SELECT * FROM datagrid WHERE kodelap = 'Lap01' "
        tes = GO()
        list_data = tes.get(query)
        self.grid_lap1.DeleteRows(len(list_data), self.grid_lap1.GetNumberRows())

        for row in range (len(list_data)):
            for col in range (len(list_data[0])-1):
                if row == 0:
                    self.grid_lap1.SetColLabelValue(col, kolom[col])
                
                val =  list_data[row][col+1]
                print('value : ' , val)
                self.grid_lap1.SetCellValue(row,col, val)


    def view_lap2(self):
        kolom = ['Kode Lap','Waktu','Nama','Tim','Tanggal','NoHP']
        query = "SELECT * FROM datagrid WHERE kodelap = 'Lap02' "
        tes = GO()
        list_data = tes.get(query)
        self.grid_lap2.DeleteRows(len(list_data), self.grid_lap2.GetNumberRows())

        for row in range (len(list_data)):
            for col in range (len(list_data[0])-1):
                if row == 0:
                    self.grid_lap2.SetColLabelValue(col, kolom[col])
                
                val =  list_data[row][col+1]
                print('value : ' , val)
                self.grid_lap2.SetCellValue(row,col, val)


    def view_lap3(self):
        kolom = ['Kode Lap','Waktu','Nama','Tim','Tanggal','NoHP']
        query = "SELECT * FROM datagrid WHERE kodelap = 'Lap03' "
        tes = GO()
        list_data = tes.get(query)
        self.grid_lap3.DeleteRows(len(list_data), self.grid_lap3.GetNumberRows())

        for row in range (len(list_data)):
            for col in range (len(list_data[0])-1):
                if row == 0:
                    self.grid_lap3.SetColLabelValue(col, kolom[col])
                
                val =  list_data[row][col+1]
                print('value : ' , val)
                self.grid_lap3.SetCellValue(row,col, val)

    
    def tbhdata(self, event):
        self.appFrame = CtrlFrame_Pesan(Frame_Pesan(None))
        self.appFrame.Show()
        self.Hide()

        

    def selectLap1(self,event):
        col = event.GetCol()
        row = event.GetRow()
        print('---lap01---')
        print('row : ' , row )
        print('col : ' , col)
        baris = row
        kode = self.grid_lap1.GetCellValue(baris,0)
        waktu = self.grid_lap1.GetCellValue(baris,1)
        nama = self.grid_lap1.GetCellValue(baris,2)
        tim = self.grid_lap1.GetCellValue(baris,3)
        tanggal = self.grid_lap1.GetCellValue(baris,4)
        nohp = self.grid_lap1.GetCellValue(baris,5)

        if col == 6:
            baris = row
            wx.MessageBox('Edit','Edit Data')
            tes = GO()
            val = (kode,waktu,nama,tim,tanggal,nohp,nama,kode)
            edit = tes.Update(val)
            print("Update data")
        elif col == 7:
            print(kode,waktu,nama,tim)
            tes = GO()
            hapus = tes.Delete(kode,waktu,nama,tim)
            wx.MessageBox('Delete : %s ,  %s , %s , %s' % (kode,waktu,nama,tim),'Berhasil Hapus Data' )
            print('Data di Hapus')
            go = CtrlFrame_Pesan(Frame_Pesan)
            self.Hide()
            return go.onmenuPesanan(event)

    def selectLap2(self,event):
        col = event.GetCol()
        row = event.GetRow()

        print('---lap02---')
        print('row : ' , row )
        print('col : ' , col)
        baris = row
        kode = self.grid_lap2.GetCellValue(baris,0)
        waktu = self.grid_lap2.GetCellValue(baris,1)
        nama = self.grid_lap2.GetCellValue(baris,2)
        tim = self.grid_lap2.GetCellValue(baris,3)
        tanggal = self.grid_lap2.GetCellValue(baris,4)
        nohp = self.grid_lap2.GetCellValue(baris,5)


        if col == 6:
            wx.MessageBox('Edit','Edit Data')
            baris = row
            wx.MessageBox('Edit','Edit Data')
            tes = GO()
            val = (kode,waktu,nama,tim,tanggal,nohp,nama,kode)
            edit = tes.Update(val)
            print("Update data")
    
        elif col == 7:
            baris = row
            tes = GO()
            hapus = tes.Delete(kode,waktu,nama,tim)
            wx.MessageBox('Delete : %s ,  %s , %s ,%s' % (kode,waktu,nama,tim),'Berhasil Hapus Data' )
            print('Data di Hapus')
            
            go = CtrlFrame_Pesan(Frame_Pesan)
            self.Hide()
            return go.onmenuPesanan(event)

    def selectLap3(self,event):
        col = event.GetCol()
        row = event.GetRow()
        print('---lap03---')
        print('row : ' , row )
        print('col : ' , col)
        baris = row
        kode = self.grid_lap3.GetCellValue(baris,0)
        waktu = self.grid_lap3.GetCellValue(baris,1)
        nama = self.grid_lap3.GetCellValue(baris,2)
        tim = self.grid_lap3.GetCellValue(baris,3)
        tanggal = self.grid_lap3.GetCellValue(baris,4)
        nohp = self.grid_lap3.GetCellValue(baris,5)


        if col == 6:
            wx.MessageBox('Edit','Edit Data')
            baris = row
            wx.MessageBox('Edit','Edit Data')
            tes = GO()
            val = (kode,waktu,nama,tim,tanggal,nohp,nama,kode)
            edit = tes.Update(val)
            print("Update data")
    
        elif col == 7:
            baris = row
            tes = GO()
            hapus = tes.Delete(kode,waktu,nama,tim)
            wx.MessageBox('Delete : %s ,  %s , %s ,%s' % (kode,waktu,nama,tim),'Berhasil Hapus Data' )
            print('Data di Hapus')

            go = CtrlFrame_Pesan(Frame_Pesan)
            self.Hide()
            return go.onmenuPesanan(event)
############################# Dialog Frame_Data ###########################


