while True:
    print("="*50)
    print("A. Buat file text (format : bil1|bil2 )")
    print("B. Lihat file text")
    print("C. Cetak hasil ")
    print("D. Selesai")
    first = input("Pilih : ")
    print("-"*50)
    try:
        if (first == "A") or (first == "a"):
            letakan = str(input("Anda ingin menyimpan dimana (contoh: e:\\. . ..txt) : "))
            myfile  = open(letakan,"a+")
            while True:
                masukan = str(input("Masukan bilangan berformat bil1|bil2 : "))
                myfile.write(masukan)
                myfile.write("\n")
                myfile.seek(0,0)
                lagi = str(input("Tambahkan lagi? (y/n) "))
                if (lagi == "y") or (lagi == "Y"):
                    continue
                else:
                    myfile.close()
                    break
        elif (first == "B") or (first == "b"):
            print("\nFile tersimpan di ",letakan,"\n")
            myfile = open(letakan,"r")
            print(myfile.read())
            myfile.close()
        elif (first == "C") or (first == "c"):
            save = str(input("File akan disimpan di ? contoh: e:\\. . ..txt : "))
            myfile = open(letakan,"r")
            isi = myfile.readlines()
            output = open(save,"w")
            for data in isi:
                angka = data.split("|")
                jumlah = int(angka[0]) + int(angka[1])
                output.write(str(jumlah))
                output.write("\n")
            myfile.close()
            output.close()
            print("\nFile berhasil disimpan. Silahkan buka file di ",save,"\n")
        elif (first == "D"):
            print("TERIMA KASIH")
            break
        else:
            print("\nPilih sesuai opsi yang tersedia.")
    except NameError:
        print("\nAnda harus membuat file text pada opsi A terlebih dahulu")
    except IndexError:
        print("\nAngka yang anda masukan pada opsi A tidak sesuai format. Pilih SELESAI, kemudian mulai ulang program.")
    except PermissionError:
        print("\nMasukan lokasi penyimpanan sesuai lokal disk yang tersedia.")
    except FileNotFoundError:
        print("\nDirektori penyimpanan tidak bisa ditemukan.")
    except ValueError:
        print("Input dalam opsi A salah. Anda harus mulai ulang program!")