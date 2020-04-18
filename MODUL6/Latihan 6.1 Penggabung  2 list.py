#Latihan 6.1
def gabungDuaListUrut(A, B):
    la = len (A)
    lb = len (B)
    C = []
    i = 0
    j = 0

    while i < la and j<lb:
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j +=1
    while i < la:
        C.append(A[i])
        i += 1
    while j < lb:
        C.append(B[j])
        j +=1
    return C
        
