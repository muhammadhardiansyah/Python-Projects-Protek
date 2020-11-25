data_sayur = ["bayam","kangkung","wortel","selada"]

while True:
    print("="*33)
    print("DATA SAYURAN")
    print("-"*33)
    A = print("A. Tambah data sayur")
    B = print("B. Hapus data sayur")
    C = print("C. Tampilkan data sayur")
    D = print("D. Tutup program")
    pilih = input("Pilihan Anda: ")
    print("-"*33)
    while True:
        if (pilih == "A"):
            tambah = str(input("Tambahkan: "))
            print("-"*33)
            data_sayur.append(tambah)
            lagi = input("Tambahkan lagi? y/n : ")
            if (lagi == "y"):
                continue
            else:
                break
        elif (pilih == "B"):
            cari = str(input("Data yang ingin dihapus: "))
            ada = cari in data_sayur
            if (ada == True):
                data_sayur.remove(cari)
                lagi = input("Hapus lagi? y/n : ")
                if (lagi == "y"):
                    continue
                else:
                    break
                
            elif (ada == False):
                print("Data tidak ditemukan")
                lagi = input("Hapus lagi? y/n : ")
                if (lagi == "y"):
                    continue
                else:
                    break
        elif (pilih == "C"):
            print(data_sayur)
            lagi = input("Lihat lagi? y/n : ")
            if (lagi == "y"):
                continue
            else:
                break
        elif (pilih == "D"):
            break
        else:
            break
    if (pilih == "D"):
        print("--- TERIMAKASIH ---")
        print("-"*33)
        break
    else:
        continue