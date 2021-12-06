import sqlite3 as sql

class veritabani():
    def __init__(self,isim):
        self.isim = isim
        self.vt = sql.connect(self.isim)            
        self.imlec = self.vt.cursor()
    
    def tabloOlustur(self,tabloAdi,kolonAd,kolonAd2):
        self.imlec.execute(f"Create table {tabloAdi} ({kolonAd},{kolonAd2})")
        self.vt.commit()
    
    def tabloyaVeriGir(self,tabloAdi,isim,soyisim):
        ## self.imlec.execute(f"insert into {tabloAdi} values ('{isim}','{soyisim}')")
        
        sorgu = f"""  insert into {tabloAdi} values(?,?) """
        self.imlec.execute(sorgu,(isim,soyisim))
        self.vt.commit()    
    
    def verileriListele(self,tabloAdi):
        self.imlec.execute(f"Select * from {tabloAdi}")
        veriler = self.imlec.fetchall()
        print("Geriye değer olarak donduruldu")
        return veriler

    def tabloSil(self,tabloAdi):
        self.imlec.execute(f"Drop table {tabloAdi}")
        print("Tablo silindi !")

