from no02 import Manusia
class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dai class Manusia"""
    matkul=[]
    def __init__(self,nama,NIM,kota,us):
        self.nama=nama
        self.NIM=NIM
        self.kota=kota
        self.uang=us
    def __str__(self):
        s=self.nama+',NIM '+str(self.NIM)\
           +'. tinggal di '+self.kota\
           +'. uang saku Rp '+str(self.uang)\
           +'. tiap bulan'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUang(self):
        return self.uang
    def makan(self,s):
        print ("saya baru saja makan",s,"sambil belajar")
        self.keadaan='kenyang'
    def ambilKota(self):
        return self.kota
    def perbaruiKota(self,k):
        self.kota=k
    def tambahUang(self,n):
        self.uang+=n
    def ambilMK(self, mk):
        return self.matkul.append(mk)
    def listKuliah(self):
        print(self.matkul)
    def hapusKuliah(self, mk):
        return self.matkul.remove(mk)

mh3 = Mahasiswa("aa","aa","aa","aa")
mh3.ambilMK("Diskrit")
mh3.listKuliah()
mh3.ambilMK("Algostruk")
mh3.listKuliah()
mh3.hapusKuliah("Diskrit")
mh3.listKuliah()
