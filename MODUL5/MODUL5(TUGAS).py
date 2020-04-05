###### Nomer 1 ######

class MhsTIF(object):
    def __init__(self, nama, umur, kota, NIM):
        self.nama = nama
        self.umur = umur
        self.kotaTinggal = kota
        self.nim = NIM

    def __str__(self):
        x = self.nim
        return x

    def getnim(self):
        return self.nim

c0 = MhsTIF('Suryo Pramuda', 23, 'Sragen', 'L200180053')
c1 = MhsTIF('Alfian', 19, 'Sumberlawang', 'L200180054')
c2 = MhsTIF('Willi susanti', 19, 'Kudus', 'L200180060')
c3 = MhsTIF('Wulandari', 19, 'Kartasura', 'L200180091')
c4 = MhsTIF('Ayudhia', 19, 'Surakarta', 'L200180095')
c5 = MhsTIF('Annisa', 20, 'Sukoharjo', 'L200180066')
c6 = MhsTIF('Nayu', 20, 'Surakarta', 'L200180099')
c7 = MhsTIF('Akbar', 21, 'Madiun', 'L200180078')
c8 = MhsTIF('Beni', 20, 'Karanganyar', 'L200180079')
c9 = MhsTIF('Rey', 21, 'Mojosongo', 'L200180087')
c10 = MhsTIF('Anggit', 20, 'Surakarta', 'L200180111')

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai.nim < A[pos - 1].nim:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai

def cetakDaftar(d):
    for i in d:
        print (i)
        

###### Nomer 2 ######

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai

######## Nomer 3 ######
from time import time as detak
from random import shuffle as kocok

def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
               swap(A,j,j+1)
               
def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiYangTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[i] < A[posisiYangTerkecil]:
            posisiYangTerkecil = i
    return posisiYangTerkecil

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i:
            swap(A, i, indexKecil)

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai

