##Swap
def swap(A,p,q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

####cariPosisiTerkecil
##def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
##    posisiYangTerkecil = dariSini
##    for i in range(dariSini+1, sampaiSini):
##        if A[i] < A[posisiYangTerkecil]:
##            posisiYangTerkecil = i
##    return posisiYangTerkecil
##
####BubbleSort
##def bubbleSort(A):
##    n = len(A)
##    for i in range(n-1):
##        for j in range(n-i-1):
##            if A[j] > A[j+1]:
##                A[j], A[j+1] = A[j+1], A[j]
##                for i in range(len(A)):
##                    print(A[i])
##                break
##        break
##
####SelectionSort
##def selectionSort(A):
##    n = len(A)
##    for i in range(n-1):
##        indexKecil = cariPosisiYangTerkecil(A, i, n)
##        if indexKecil != i:
##            swap(A, i, indexKecil)
##
##
####InsertionSort
##def insertionsort(a):
##    for i in range(1,len(a)):
##        nilai = a[i]
##        b = i
##        while b >0 and nilai<a[b - 1]:
##            a[b]=a[b-1]
##            b -=1
##        a[b]=nilai
##P=[10,51,2,18,4,31,13,5,23,64,29]
