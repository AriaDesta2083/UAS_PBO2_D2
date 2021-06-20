import mysql.connector

class DATABASE:
  def __init__(self):
      self.db =  mysql.connector.connect( 
          host = "localhost", 
          user = "root", 
          password = "", 
          database = "pbo",
          )
      self.connect = self.db.cursor()

  def connection(self,query,retval=False):
      self.connect.execute(query)
      all_result = self.connect.fetchall()
      self.db.commit()
      if retval:
          return all_result

class GO(DATABASE):
  def get(self,goquery):
    self.query = goquery
    Connection = self.connection(self.query,True)
    return Connection


  def Insert_Grid(self,val):
    self.query =  "INSERT INTO `datagrid` (`id`, `kodelap`, `waktu`, `nama`, `tim`, `tanggal`, `nohp`) VALUES(NULL,%s,%s,%s,%s,%s,%s)"
    self.connect.execute(self.query , val )
    self.db.commit()
    print("{} data berhasil ditambahkan".format(self.connect.rowcount))
  
  def Delete(self,kode,waktu,nama,tim):
    self.query = "DELETE FROM datagrid WHERE kodelap = '%s' AND waktu = '%s' AND nama = '%s' AND tim = '%s'"
    self.query = self.query % (kode,waktu,nama,tim)
    self.connect.execute(self.query)
    self.db.commit()
    print("{} data berhasil dihapus".format(self.connect.rowcount))

  def Update(self,val):
    self.query = "UPDATE datagrid SET kodelap = %s , waktu = %s, nama = %s , tim  = %s , tanggal = %s , nohp = %s WHERE datagrid.nama = %s AND datagrid.kodelap = %s"
    self.connect.execute(self.query , val )
    self.db.commit()
    print("{} data berhasil diupdate".format(self.connect.rowcount))
      

