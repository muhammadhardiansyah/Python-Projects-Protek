buah = { "apel" : 5000,
         "jeruk": 8500,
         "mangga":7800,
         "duku" : 6500}
print("="*33)
print("-"*10,"BUAH SEGAR","-"*10)
print("="*33)
total_harga=0
while True:
    print("-"*33)
    nama_buah = str(input("Nama buah yang ingin dibeli  : "))
    ada = nama_buah in buah
    if (ada == True):
        for x,y in buah.items():
            x
            if(x == nama_buah):
                kg = float(input("Berapa kg                    : "))
                harga = kg * y
        total_harga += harga
        lagi = input("Beli buah yang lain? y/n : ")
        if (lagi == "y"):
            continue
        else:
            break
    elif(ada != True):
        print("Buah tidak ada")
    
    
            
print("-"*40)
print("Total harga                  : Rp.",total_harga)
     








