def unCaesar(huruf,n):
    a = ord((huruf))
    b = a - n
    c = chr(b)
    return c

while True:
    print("="*50)
    print("A. Masukan file terenskripsi sandi caesar")
    print("B. Ubah menjadi normal")
    print("C. Selesai")
    first = str(input("Pilihan : "))
    print("-"*50)
    try:
        if (first == "A") or (first == "a"):
            cari = str(input("Masukan file: (contoh: e:\\__.txt) : "))
            myfile = open(cari,"r")
            myfile.close()
        elif (first == "B") or (first == "b"):
            print("\n!!!   Jika bilangan di enskripsikan 2, maka masukan 2")
            print("      Jangan tambahkan negatif.                      !!!\n")
            geser = int(input("Enskripsikan sejauh? (Bil. Bulat) : "))
            n = geser % 26
            save = str(input("File akan disimpan di? Contoh : e:\\___.txt : "))
            myfile = open(cari,"r")
            output = open(save,"w")
            char = myfile.read()
            charUp= char.upper()
            listChar = list(charUp)
            for teks in listChar:
                angka = ord(teks)
                if (teks.isalpha()) and (angka - n >= 65):
                    output.write(unCaesar(teks,n))
                elif (teks.isalpha()) and (angka - n < 65):
                    x   = angka - n
                    y   = 65 - x
                    new = 91 - y 
                    output.write(chr(new))
                else:
                    output.write(" ")
            myfile.close()
            output.close()
        elif (first == "C") or (first == "c"):
            break
        else:
            print("Pilihlah sesuai opsi yang tersedia.")
    except NameError:
        print("\nAnda harus mencari file text pada opsi A terlebih dahulu")
    except IndexError:
        print("\nAngka yang anda masukan pada opsi A tidak sesuai format. Pilih SELESAI, kemudian mulai ulang program.")
    except PermissionError:
        print("\nMasukan lokasi penyimpanan sesuai lokal disk yang tersedia dan jangan masukkan pada disk system.")
    except FileNotFoundError:
        print("\nDirektori penyimpanan tidak bisa ditemukan.")
    except ValueError:
        print("\nBilangan yang anda masukkan tidak valid")