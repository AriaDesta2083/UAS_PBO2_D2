# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class Frame_Pesan
###########################################################################

class Frame_Pesan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"GLADIATOR FUTSAL", pos = wx.DefaultPosition, size = wx.Size( 1000,680 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( -1,-1 ), wx.Size( 1000,680 ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.Colour( 21, 35, 100 ) )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_open = wx.Menu()
		self.datapesanan = wx.MenuItem( self.m_open, wx.ID_ANY, u"Data Pesanan", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_open.Append( self.datapesanan )

		self.m_menubar1.Append( self.m_open, u"Open" )

		self.SetMenuBar( self.m_menubar1 )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		self.judul = wx.StaticText( self, wx.ID_ANY, u"Booking Lapangan Futsal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.judul.Wrap( -1 )

		self.judul.SetFont( wx.Font( 24, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Century Gothic" ) )
		self.judul.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		bSizer7.Add( self.judul, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		bSizer1.Add( bSizer7, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 35 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.kode_lap = wx.StaticText( self, wx.ID_ANY, u"Kode Lapangan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.kode_lap.Wrap( -1 )

		self.kode_lap.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century Gothic" ) )
		self.kode_lap.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer1.Add( self.kode_lap, 0, wx.ALL, 5 )

		input_codeChoices = [ u"Lap01", u"Lap02", u"Lap03" ]
		self.input_code = wx.ComboBox( self, wx.ID_ANY, u"Lap01", wx.DefaultPosition, wx.DefaultSize, input_codeChoices, wx.CB_READONLY )
		self.input_code.SetSelection( 0 )
		self.input_code.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century Gothic" ) )
		self.input_code.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.input_code.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer1.Add( self.input_code, 0, wx.ALL, 5 )

		self.tanggal = wx.StaticText( self, wx.ID_ANY, u"Tanggal Pemesanan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tanggal.Wrap( -1 )

		self.tanggal.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century Gothic" ) )
		self.tanggal.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer1.Add( self.tanggal, 0, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.LEFT, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.tanggal = wx.SpinCtrl( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 31, 5 )
		self.tanggal.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century Gothic" ) )
		self.tanggal.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		bSizer4.Add( self.tanggal, 0, wx.ALL|wx.EXPAND, 5 )

		bulanChoices = [ u"Januari", u"Februari", u"Maret", u"April", u"Mei", u"Juni", u"Juli", u"Agustus", u"September", u"Oktober", u"November", u"Desember" ]
		self.bulan = wx.ComboBox( self, wx.ID_ANY, u"April", wx.DefaultPosition, wx.DefaultSize, bulanChoices, wx.CB_DROPDOWN|wx.CB_READONLY )
		self.bulan.SetSelection( 3 )
		self.bulan.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century Gothic" ) )
		self.bulan.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		bSizer4.Add( self.bulan, 0, wx.ALL, 5 )

		self.tahun = wx.SpinCtrl( self, wx.ID_ANY, u"2021", wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 2021, 9999, 2021 )
		self.tahun.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century Gothic" ) )
		self.tahun.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		bSizer4.Add( self.tahun, 0, wx.ALL, 5 )


		fgSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )

		self.waktu = wx.StaticText( self, wx.ID_ANY, u"Waktu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.waktu.Wrap( -1 )

		self.waktu.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century Gothic" ) )
		self.waktu.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer1.Add( self.waktu, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

		waktu_awalChoices = [ u"07:00", u"08:00", u"09:00", u"10:00", u"11:00", u"12:00", u"13:00", u"14:00", u"15:00", u"16:00", u"17:00", u"18:00", u"19:00", u"20:00", u"21:00", u"22:00", u"23:00" ]
		self.waktu_awal = wx.ComboBox( self, wx.ID_ANY, u"10:00", wx.DefaultPosition, wx.DefaultSize, waktu_awalChoices, wx.CB_READONLY )
		self.waktu_awal.SetSelection( 3 )
		self.waktu_awal.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century Gothic" ) )
		self.waktu_awal.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		bSizer3.Add( self.waktu_awal, 0, wx.ALL, 5 )


		bSizer3.Add( ( 0, 0), 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 25 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"sampai", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		self.m_staticText5.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century Gothic" ) )
		self.m_staticText5.SetForegroundColour( wx.Colour( 244, 227, 77 ) )

		bSizer3.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		waktu_akhirChoices = [ u"08:00", u"09:00", u"10:00", u"11:00", u"12:00", u"13:00", u"14:00", u"15:00", u"16:00", u"17:00", u"18:00", u"19:00", u"20:00", u"21:00", u"22:00", u"23:00", u"24:00" ]
		self.waktu_akhir = wx.ComboBox( self, wx.ID_ANY, u"08:00", wx.DefaultPosition, wx.DefaultSize, waktu_akhirChoices, wx.CB_READONLY )
		self.waktu_akhir.SetSelection( 0 )
		self.waktu_akhir.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century Gothic" ) )
		self.waktu_akhir.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		bSizer3.Add( self.waktu_akhir, 0, wx.ALL, 5 )


		fgSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Nama Pemesan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		self.m_staticText6.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century Gothic" ) )
		self.m_staticText6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer1.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.input_nama = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.input_nama.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century Gothic" ) )
		self.input_nama.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		fgSizer1.Add( self.input_nama, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Nama Team", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		self.m_staticText8.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century Gothic" ) )
		self.m_staticText8.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer1.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.input_tim = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.input_tim.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century Gothic" ) )
		self.input_tim.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		fgSizer1.Add( self.input_tim, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"No Handphone", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century Gothic" ) )
		self.m_staticText7.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )

		fgSizer1.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.input_nohp = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.input_nohp.SetMaxLength( 12 )
		self.input_nohp.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century Gothic" ) )
		self.input_nohp.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		fgSizer1.Add( self.input_nohp, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALL, 5 )


		bSizer2.Add( fgSizer1, 0, 0, 5 )


		bSizer1.Add( bSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 35 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )

		self.pesan = wx.Button( self, wx.ID_ANY, u"Pesan", wx.DefaultPosition, wx.Size( 270,-1 ), 0 )
		self.pesan.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Century Gothic" ) )
		self.pesan.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.pesan.SetBackgroundColour( wx.Colour( 244, 227, 77 ) )

		bSizer18.Add( self.pesan, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )

		self.hapus_semua = wx.Button( self, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		self.hapus_semua.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Century Gothic" ) )
		self.hapus_semua.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.hapus_semua.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer18.Add( self.hapus_semua, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )


		bSizer5.Add( bSizer18, 0, wx.TOP|wx.BOTTOM|wx.RIGHT, 26 )


		bSizer1.Add( bSizer5, 1, wx.ALIGN_RIGHT|wx.RIGHT, 100 )


		self.SetSizer( bSizer1 )
		self.Layout()

		# Connect Events
		self.Bind( wx.EVT_MENU, self.onmenuPesanan, id = self.datapesanan.GetId() )
		self.pesan.Bind( wx.EVT_BUTTON, self.onPesan )
		self.hapus_semua.Bind( wx.EVT_BUTTON, self.onHapus )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onmenuPesanan( self, event ):
		event.Skip()

	def onPesan( self, event ):
		event.Skip()

	def onHapus( self, event ):
		event.Skip()


###########################################################################
## Class Frame_Login
###########################################################################

class Frame_Login ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 900,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( -1,-1 ), wx.Size( -1,-1 ) )
		self.SetBackgroundColour( wx.Colour( 21, 35, 100 ) )

		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.judul = wx.StaticText( self, wx.ID_ANY, u"GLADIATOR FUTSAL", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.judul.Wrap( -1 )

		self.judul.SetFont( wx.Font( 26, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, True, "Century Gothic" ) )
		self.judul.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.judul.SetBackgroundColour( wx.Colour( 21, 35, 100 ) )

		bSizer11.Add( self.judul, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 25 )


		bSizer10.Add( bSizer11, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM, 0 )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		self.username = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.username.Wrap( -1 )

		self.username.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century Gothic" ) )
		self.username.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.username.SetBackgroundColour( wx.Colour( 21, 35, 100 ) )

		gSizer2.Add( self.username, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.input_username = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_BESTWRAP|wx.TE_CENTER|wx.TE_PROCESS_ENTER )
		self.input_username.SetMaxLength( 100 )
		self.input_username.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century Gothic" ) )
		self.input_username.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.input_username.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		gSizer2.Add( self.input_username, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.password = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.password.Wrap( -1 )

		self.password.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century Gothic" ) )
		self.password.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.password.SetBackgroundColour( wx.Colour( 21, 35, 100 ) )

		gSizer2.Add( self.password, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.input_password = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), wx.TE_BESTWRAP|wx.TE_CENTER|wx.TE_PASSWORD|wx.TE_PROCESS_ENTER )
		self.input_password.SetMaxLength( 8 )
		self.input_password.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century Gothic" ) )
		self.input_password.SetForegroundColour( wx.Colour( 234, 221, 15 ) )
		self.input_password.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		gSizer2.Add( self.input_password, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 25 )


		bSizer10.Add( gSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL, 100 )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.login_user = wx.Button( self, wx.ID_ANY, u"LOGIN", wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.login_user.SetFont( wx.Font( 16, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Century Gothic" ) )
		self.login_user.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.login_user.SetBackgroundColour( wx.Colour( 234, 211, 15 ) )

		bSizer13.Add( self.login_user, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 25 )


		bSizer10.Add( bSizer13, 0, wx.ALIGN_CENTER_HORIZONTAL, 15 )


		bSizer18.Add( bSizer10, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 50 )


		self.SetSizer( bSizer18 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.login_user.Bind( wx.EVT_BUTTON, self.onloginuser )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onloginuser( self, event ):
		event.Skip()


###########################################################################
## Class Frame_Data
###########################################################################

class Frame_Data ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"GLADIATOR FUTSAL", pos = wx.DefaultPosition, size = wx.Size( 1200,680 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 1200,680 ), wx.Size( 1200,680 ) )
		self.SetBackgroundColour( wx.Colour( 21, 35, 100 ) )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Lap1 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.Lap1.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century Gothic" ) )

		bSizer121 = wx.BoxSizer( wx.VERTICAL )

		self.grid_lap1 = wx.grid.Grid( self.Lap1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.grid_lap1.CreateGrid( 10, 8 )
		self.grid_lap1.EnableEditing( True )
		self.grid_lap1.EnableGridLines( False )
		self.grid_lap1.EnableDragGridSize( False )
		self.grid_lap1.SetMargins( 0, 0 )

		# Columns
		self.grid_lap1.SetColSize( 0, 125 )
		self.grid_lap1.SetColSize( 1, 125 )
		self.grid_lap1.SetColSize( 2, 125 )
		self.grid_lap1.SetColSize( 3, 125 )
		self.grid_lap1.SetColSize( 4, 125 )
		self.grid_lap1.SetColSize( 5, 150 )
		self.grid_lap1.SetColSize( 6, 125 )
		self.grid_lap1.SetColSize( 7, 125 )
		self.grid_lap1.EnableDragColMove( True )
		self.grid_lap1.EnableDragColSize( True )
		self.grid_lap1.SetColLabelSize( 32 )
		self.grid_lap1.SetColLabelValue( 0, u"Kode Lap" )
		self.grid_lap1.SetColLabelValue( 1, u"Waktu" )
		self.grid_lap1.SetColLabelValue( 2, u"Nama" )
		self.grid_lap1.SetColLabelValue( 3, u"Tim" )
		self.grid_lap1.SetColLabelValue( 4, u"Tanggal" )
		self.grid_lap1.SetColLabelValue( 5, u"No Handphone" )
		self.grid_lap1.SetColLabelValue( 6, u"EDIT" )
		self.grid_lap1.SetColLabelValue( 7, u"DELETE" )
		self.grid_lap1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.grid_lap1.AutoSizeRows()
		self.grid_lap1.EnableDragRowSize( True )
		self.grid_lap1.SetRowLabelSize( 80 )
		self.grid_lap1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.grid_lap1.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )
		self.grid_lap1.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century Gothic" ) )

		bSizer121.Add( self.grid_lap1, 0, wx.ALL, 5 )

		bSizer1512 = wx.BoxSizer( wx.HORIZONTAL )

		self.tambah_pesanan1 = wx.Button( self.Lap1, wx.ID_ANY, u"Tambah Pesanan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tambah_pesanan1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century Gothic" ) )

		bSizer1512.Add( self.tambah_pesanan1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.hapus_pesanan = wx.Button( self.Lap1, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.hapus_pesanan.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century Gothic" ) )

		bSizer1512.Add( self.hapus_pesanan, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


		bSizer121.Add( bSizer1512, 1, wx.ALIGN_RIGHT|wx.BOTTOM|wx.RIGHT, 50 )


		self.Lap1.SetSizer( bSizer121 )
		self.Lap1.Layout()
		bSizer121.Fit( self.Lap1 )
		self.m_notebook1.AddPage( self.Lap1, u"Lapangan 01", True )
		self.Lap2 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.Lap2.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century Gothic" ) )

		bSizer122 = wx.BoxSizer( wx.VERTICAL )

		self.grid_lap2 = wx.grid.Grid( self.Lap2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.grid_lap2.CreateGrid( 10, 8 )
		self.grid_lap2.EnableEditing( True )
		self.grid_lap2.EnableGridLines( False )
		self.grid_lap2.EnableDragGridSize( False )
		self.grid_lap2.SetMargins( 0, 0 )

		# Columns
		self.grid_lap2.SetColSize( 0, 125 )
		self.grid_lap2.SetColSize( 1, 125 )
		self.grid_lap2.SetColSize( 2, 125 )
		self.grid_lap2.SetColSize( 3, 125 )
		self.grid_lap2.SetColSize( 4, 125 )
		self.grid_lap2.SetColSize( 5, 150 )
		self.grid_lap2.SetColSize( 6, 125 )
		self.grid_lap2.SetColSize( 7, 125 )
		self.grid_lap2.EnableDragColMove( False )
		self.grid_lap2.EnableDragColSize( True )
		self.grid_lap2.SetColLabelSize( 32 )
		self.grid_lap2.SetColLabelValue( 0, u"Kode Lap" )
		self.grid_lap2.SetColLabelValue( 1, u"Waktu" )
		self.grid_lap2.SetColLabelValue( 2, u"Nama" )
		self.grid_lap2.SetColLabelValue( 3, u"Tim" )
		self.grid_lap2.SetColLabelValue( 4, u"Tanggal" )
		self.grid_lap2.SetColLabelValue( 5, u"No Handphone" )
		self.grid_lap2.SetColLabelValue( 6, u"EDIT" )
		self.grid_lap2.SetColLabelValue( 7, u"DELETE" )
		self.grid_lap2.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.grid_lap2.AutoSizeRows()
		self.grid_lap2.EnableDragRowSize( True )
		self.grid_lap2.SetRowLabelSize( 80 )
		self.grid_lap2.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.grid_lap2.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )
		bSizer122.Add( self.grid_lap2, 0, wx.ALL, 5 )

		bSizer151 = wx.BoxSizer( wx.HORIZONTAL )

		self.tambah_pesanan2 = wx.Button( self.Lap2, wx.ID_ANY, u"Tambah Pesanan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tambah_pesanan2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century Gothic" ) )

		bSizer151.Add( self.tambah_pesanan2, 0, wx.ALIGN_BOTTOM|wx.ALL, 5 )

		self.hapus_pesanan1 = wx.Button( self.Lap2, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.hapus_pesanan1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century Gothic" ) )

		bSizer151.Add( self.hapus_pesanan1, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


		bSizer122.Add( bSizer151, 1, wx.ALIGN_RIGHT|wx.BOTTOM|wx.RIGHT, 50 )


		self.Lap2.SetSizer( bSizer122 )
		self.Lap2.Layout()
		bSizer122.Fit( self.Lap2 )
		self.m_notebook1.AddPage( self.Lap2, u"Lapangan 02", False )
		self.Lap3 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.Lap3.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century Gothic" ) )

		bSizer1221 = wx.BoxSizer( wx.VERTICAL )

		self.grid_lap3 = wx.grid.Grid( self.Lap3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.grid_lap3.CreateGrid( 10, 8 )
		self.grid_lap3.EnableEditing( True )
		self.grid_lap3.EnableGridLines( False )
		self.grid_lap3.EnableDragGridSize( False )
		self.grid_lap3.SetMargins( 0, 0 )

		# Columns
		self.grid_lap3.SetColSize( 0, 125 )
		self.grid_lap3.SetColSize( 1, 125 )
		self.grid_lap3.SetColSize( 2, 125 )
		self.grid_lap3.SetColSize( 3, 125 )
		self.grid_lap3.SetColSize( 4, 125 )
		self.grid_lap3.SetColSize( 5, 150 )
		self.grid_lap3.SetColSize( 6, 125 )
		self.grid_lap3.SetColSize( 7, 125 )
		self.grid_lap3.EnableDragColMove( False )
		self.grid_lap3.EnableDragColSize( True )
		self.grid_lap3.SetColLabelSize( 32 )
		self.grid_lap3.SetColLabelValue( 0, u"Kode Lap" )
		self.grid_lap3.SetColLabelValue( 1, u"Waktu" )
		self.grid_lap3.SetColLabelValue( 2, u"Nama" )
		self.grid_lap3.SetColLabelValue( 3, u"Tim" )
		self.grid_lap3.SetColLabelValue( 4, u"Tanggal" )
		self.grid_lap3.SetColLabelValue( 5, u"No Handphone" )
		self.grid_lap3.SetColLabelValue( 6, u"EDIT" )
		self.grid_lap3.SetColLabelValue( 7, u"DELETE" )
		self.grid_lap3.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.grid_lap3.AutoSizeRows()
		self.grid_lap3.EnableDragRowSize( True )
		self.grid_lap3.SetRowLabelSize( 80 )
		self.grid_lap3.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.grid_lap3.SetDefaultCellAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )
		self.grid_lap3.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century Gothic" ) )

		bSizer1221.Add( self.grid_lap3, 0, wx.ALL, 5 )

		bSizer1511 = wx.BoxSizer( wx.HORIZONTAL )

		self.tambah_pesanan3 = wx.Button( self.Lap3, wx.ID_ANY, u"Tambah Pesanan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tambah_pesanan3.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century Gothic" ) )

		bSizer1511.Add( self.tambah_pesanan3, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		self.hapus_pesanan = wx.Button( self.Lap3, wx.ID_ANY, u"Hapus", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.hapus_pesanan.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Century Gothic" ) )

		bSizer1511.Add( self.hapus_pesanan, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )


		bSizer1221.Add( bSizer1511, 1, wx.ALIGN_RIGHT|wx.BOTTOM|wx.RIGHT, 50 )


		self.Lap3.SetSizer( bSizer1221 )
		self.Lap3.Layout()
		bSizer1221.Fit( self.Lap3 )
		self.m_notebook1.AddPage( self.Lap3, u"Lapangan 03", False )

		bSizer11.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer11 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_notebook1.Bind( wx.EVT_NOTEBOOK_PAGE_CHANGED, self.print_data )
		self.grid_lap1.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.selectLap1 )
		self.tambah_pesanan1.Bind( wx.EVT_BUTTON, self.tbhdata )
		self.hapus_pesanan.Bind( wx.EVT_BUTTON, self.onDataHapus )
		self.grid_lap2.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.selectLap2 )
		self.tambah_pesanan2.Bind( wx.EVT_BUTTON, self.tbhdata )
		self.grid_lap3.Bind( wx.grid.EVT_GRID_SELECT_CELL, self.selectLap3 )
		self.tambah_pesanan3.Bind( wx.EVT_BUTTON, self.tbhdata )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def print_data( self, event ):
		event.Skip()

	def selectLap1( self, event ):
		event.Skip()

	def tbhdata( self, event ):
		event.Skip()

	def onDataHapus( self, event ):
		event.Skip()

	def selectLap2( self, event ):
		event.Skip()


	def selectLap3( self, event ):
		event.Skip()



###########################################################################
## Class dialog_loginberhasil
###########################################################################

class dialog_loginberhasil ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 224,143 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Century Gothic" ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Login Berhasil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Century Gothic" ) )

		bSizer20.Add( self.m_staticText13, 0, wx.ALIGN_CENTER_HORIZONTAL, 25 )


		bSizer19.Add( bSizer20, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 20 )

		m_sdbSizer2 = wx.StdDialogButtonSizer()
		self.m_sdbSizer2OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer2.AddButton( self.m_sdbSizer2OK )
		m_sdbSizer2.Realize();

		bSizer19.Add( m_sdbSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		self.SetSizer( bSizer19 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_sdbSizer2OK.Bind( wx.EVT_BUTTON, self.onloginberhasil )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onloginberhasil( self, event ):
		event.Skip()


###########################################################################
## Class dialog_logingagal
###########################################################################

class dialog_logingagal ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 224,143 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Century Gothic" ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Login Gagal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Century Gothic" ) )

		bSizer20.Add( self.m_staticText13, 0, wx.ALIGN_CENTER_HORIZONTAL, 25 )


		bSizer19.Add( bSizer20, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 20 )

		m_sdbSizer2 = wx.StdDialogButtonSizer()
		self.m_sdbSizer2OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer2.AddButton( self.m_sdbSizer2OK )
		m_sdbSizer2.Realize();

		bSizer19.Add( m_sdbSizer2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		self.SetSizer( bSizer19 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_sdbSizer2OK.Bind( wx.EVT_BUTTON, self.onlogingagal )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onlogingagal( self, event ):
		event.Skip()


###########################################################################
## Class dialog_pesan
###########################################################################

class dialog_pesan ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Century Gothic" ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Pesanan Ditambahkan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Century Gothic" ) )

		bSizer20.Add( self.m_staticText13, 0, wx.ALIGN_CENTER_HORIZONTAL, 25 )


		bSizer19.Add( bSizer20, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 25 )

		m_sdbSizer2 = wx.StdDialogButtonSizer()
		self.m_sdbSizer2OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer2.AddButton( self.m_sdbSizer2OK )
		m_sdbSizer2.Realize();

		bSizer19.Add( m_sdbSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		self.SetSizer( bSizer19 )
		self.Layout()
		bSizer19.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_sdbSizer2OK.Bind( wx.EVT_BUTTON, self.ondialog_pesan )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def ondialog_pesan( self, event ):
		event.Skip()


###########################################################################
## Class dialog_hapus
###########################################################################

class dialog_hapus ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 266,168 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Pesanan Akan Dihapus?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		self.m_staticText13.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Century Gothic" ) )

		bSizer20.Add( self.m_staticText13, 0, wx.ALIGN_CENTER_HORIZONTAL, 25 )


		bSizer19.Add( bSizer20, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 25 )

		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
		self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();

		bSizer19.Add( m_sdbSizer1, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )


		self.SetSizer( bSizer19 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_sdbSizer1Cancel.Bind( wx.EVT_BUTTON, self.ondialog_cancel )
		self.m_sdbSizer1OK.Bind( wx.EVT_BUTTON, self.ondialog_hapus )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def ondialog_cancel( self, event ):
		event.Skip()

	def ondialog_hapus( self, event ):
		event.Skip()


