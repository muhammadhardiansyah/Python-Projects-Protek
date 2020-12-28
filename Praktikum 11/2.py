from datetime import datetime
from datetime import date
from datetime import timedelta
while True:
    try:
        print("="*50)
        print("A. Buat file")
        print("B. Isi Data")
        print("C. Selesai")
        pilih = input("Pilih : ")
        print("-"*50)
        if (pilih == "A") or (pilih == "a"):
            save = str(input("File ingin disimpan di: (Contoh: e:\\__.txt) : "))
            output = open(save,"w")
            output.close()
            print("\nFile berhasil dibuat di",save)
        elif (pilih == "B") or (pilih == "b"):    
            while True:
                code = str(input("Masukan Kode Member   : "))
                name = str(input("Masukan Nama Member   : "))
                book = str(input("Masukan Judul Buku    : "))
                tglNow = datetime.date(datetime.now())
                back = tglNow + timedelta(days=7)
                tulis = code + "|" + name + "|" + book + "|" + str(tglNow) + "|" + str(back)
                output = open(save,"a+")
                output.write(tulis)
                output.write("\n")
                output.seek(0,0)
                lagi = input("Masukan lagi? (y/n) : ")
                if (lagi == "Y") or (lagi == "y"):
                    continue
                elif (lagi == "N") or (lagi == "n"):
                    output.close()
                    print("\nSukses! File tersimpan di",save)
                    break
        elif (pilih == "C") or (pilih == "c"):
            print("Terima Kasih")
            break
    except NameError:
        print("\nAnda harus membuat file text pada opsi A terlebih dahulu")
    except IndexError:
        print("\nNilai salah")
    except PermissionError:
        print("\nMasukan lokasi penyimpanan sesuai lokal disk yang tersedia dan jangan masukkan pada disk system.")
    except FileNotFoundError:
        print("\nDirektori penyimpanan tidak bisa ditemukan.")
    except ValueError:
        print("\nBilangan yang anda masukkan tidak valid")