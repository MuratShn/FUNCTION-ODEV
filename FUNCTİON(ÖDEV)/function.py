from databasee import veritabani 

vt = veritabani("Deneme.db")
vt.tabloSil("ogrenci")
vt.tabloOlustur("ogrenci","Isim","Soyisim")
vt.tabloyaVeriGir("ogrenci","ismail","inci")
a = vt.verileriListele("ogrenci")
print(a)
