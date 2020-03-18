from no02 import Manusia
class SiswaSMA(Manusia):
    jurusan = "Belum Ditentukan"
    univ = "Belum Ditentukan"
    def __init__(self, nama, nisn, sma):
        self.nama = nama
        self.nisn = nisn
        self.sma = sma
    def __str__(self):
        return "\n\nData Diri\n"\
               +"Nama   : "+self.nama\
               +"\nNISN   : "+str(self.nisn)\
               +"\nSMA    : "+self.sma\
               +"\nUniv Pilihan : "+self.univ\
               +"\nJurusan Pilihan : "+self.jurusan
    def ambil(self):
        print("\n\nUpdate Data Universitas Pilihan...")
        self.univ = input("Pilih Univ : ")
        self.jurusan = input("Ambil Jurusan : ")


sis = SiswaSMA("Aulia Anis","3012567845","SMA N 2 Wonogiri")
print(sis)
sis.ambil()
print(sis)
