buah = { "apel" : 5000,
         "jeruk": 8500,
         "mangga":7800,
         "duku" : 6500}
while True:
    print("="*40)
    print("PENDATAAN BUAH")
    print("-"*40)
    print("Menu:")
    print("A. Tambah data buah")
    print("B. Beli buah")
    print("C. Hapus data buah")
    print("D. Lihat data buah")
    print("E. Tutup Program\n")
    pilihan = str(input("Pilihan menu : "))
    if (pilihan == "A"):
        while True:
            nama =  str(input("Masukan nama buah  : "))
            if nama in buah:
                print("Harganya Rp.",buah[nama])
            else:
                harga = int(input("Masukan harga buah : "))
                buah [nama] = harga
                lagi = str(input("Menambahkan lagi? y/n : "))
                if (lagi == "y"):
                    continue
                else:
                    for x,y in buah.items():
                        print("- ",x,"  ( Harga Rp.",y," )")
                    break
    elif (pilihan == "B"):
        total_harga=0
        while True:
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
    
    elif (pilihan == "C"):
        while True:
            hapus = str(input("Masukan buah yang perlu dihapus : "))
            if (hapus in buah):
                del buah[hapus]
                lagi = input("Menghapus lagi? y/n : ")
                if (lagi == "y"):
                    continue
                else:
                    break
            else:
                print("Buah tidak ditemukan")
                continue

    elif (pilihan == "D"):
        for x,y in buah.items():
            print(x," harganya :",y)
    
    elif (pilihan == "E"):
        print("="*40)
        print("-"*12,"TERIMAKASIH","-"*12)
        print("="*40)
        break
    else:
        continue