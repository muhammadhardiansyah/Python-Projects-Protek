def rerata (myData):
    jumlah = 0
    count = 0
    for y in myData.values():
        jumlah += y
        count += 1
    hasil = jumlah / count
    return (hasil)



buah = { "apel" : 5000,
         "jeruk": 8500,
         "mangga":7800,
         "duku" : 6500}
print("Rata-rata harga satuan dari semua buah adalah",rerata(buah),"rupiah")
