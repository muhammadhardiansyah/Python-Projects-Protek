def Caesar(huruf,n):
    a = ord((huruf))
    b = a + n
    c = chr(b)
    return c

while True:
    print('='*50)
    print("A. Buat file asli")
    print("B. Lihat file asli")
    print("C. Enskripsikan ke sandi caesar")
    print("D. Selesai")
    first = str(input("Pilih : "))
    print("-"*50)
    try:
        if (first == "A") or (first == "a"):
            simpan = str(input("Simpan di ? Contoh (e:\\___.txt) : "))
            myfile = open(simpan,"w")
            print("fyi: Hanya abjad yang akan terenskripsi")
            tulis  = str(input("Masukan isi file tersebut:"))
            myfile.write(tulis)
            myfile.close()
        elif (first == "B") or (first == "b"):
            myfile = open(simpan,"r")
            print(myfile.read())
            myfile.close()
        elif (first  == "C") or (first == "c"):
            geser = int(input("Enskripsikan sejauh? (Bil. Bulat) : "))
            n = geser % 26
            save = str(input("File akan disimpan di? Contoh : e:\\___.txt : "))
            myfile = open(simpan,"r")
            output = open(save,"w")
            char = myfile.read()
            charUp= char.upper()
            listChar = list(charUp)
            for teks in listChar:
                angka = ord(teks)
                if (teks.isalpha()) and (angka + n <= 90):
                    output.write(Caesar(teks,n))
                elif (teks.isalpha()) and (angka + n > 90):
                    new = 64 + ((angka + n) - 90)
                    output.write(chr(new))
                else:
                    output.write(" ")
            myfile.close()
            output.close()
        elif (first == "D") or (first == "d"):
            break
        else:
            print("Pilihlah sesuai opsi yang tersedia.")
    except NameError:
        print("\nAnda harus membuat file text pada opsi A terlebih dahulu")
    except IndexError:
        print("\nAngka yang anda masukan pada opsi A tidak sesuai format. Pilih SELESAI, kemudian mulai ulang program.")
    except PermissionError:
        print("\nMasukan lokasi penyimpanan sesuai lokal disk yang tersedia dan jangan masukkan pada disk system.")
    except FileNotFoundError:
        print("\nDirektori penyimpanan tidak bisa ditemukan.")
    except ValueError:
        print("\nBilangan yang anda masukkan tidak valid")