def sum (*myData):
    jumlh = 0
    for data in myData:
        jumlh += data
    hasil = jumlh
    return hasil


def average(*myData):
    ada = 0
    for data in myData:
        ada += 1
    rerata = sum(*myData) / ada
    hasil = rerata
    return hasil


def maks (*myData):
    besar = 0
    for data in myData:
        if (data > besar):
            besar = data
    hasil = besar
    return hasil


def min (*myData):
    kecil = 100000
    for data in myData:
        if (data < kecil):
            kecil = data
    hasil = kecil
    return hasil
