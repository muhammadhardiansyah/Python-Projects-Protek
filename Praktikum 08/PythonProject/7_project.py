def mahal (daftar):
    data = list(daftar.values())
    data.sort()
    a = data[-1]
    for x,y in daftar.items():
        y
        if (y == a):
            hasil = print(x)
    return hasil
        

buah = { "apel" : 5000,
         "jeruk": 8500,
         "mangga":7800,
         "duku" : 6500}
mahal(buah)
