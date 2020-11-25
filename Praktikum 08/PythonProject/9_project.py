buah = { "apel" : 5000,
         "jeruk": 8500,
         "mangga":7800,
         "duku" : 6500}
print("="*33)
print("-"*10,"BUAH SEGAR","-"*10)
print("="*33)
print("-"*33)
nama_buah = str(input("Nama buah yang ingin dibeli  : "))
ada = nama_buah in buah
if (ada == True):
    for x,y in buah.items():
        x
        if(x == nama_buah):
            kg = float(input("Berapa kg                    : "))
            harga = y * kg
    print("-"*40)
    print("Total harga                  : Rp.",harga)
else:
    print("Buah tidak ada")
     








