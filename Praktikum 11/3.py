from datetime import datetime
from datetime import date
from datetime import timedelta

def diffDate(x):
    tglNew = date(year = int(x[0]), month = int(x[1]), day = int(x[2]))
    tglNow = datetime.date(datetime.now())
    selisih= tglNow - tglNew
    if ("days" in str(selisih)):
        selisihTgl= str(selisih).replace("days, 0:00:00","")
    elif ("day" in str(selisih)):
        selisihTgl= str(selisih).replace("day, 0:00:00","")
    else:
        selisihTgl= str(selisih).replace("0:00:00","0")
    hasil = int(selisihTgl)
    return hasil

while True:
    try:
        print("="*50)
        print("A. Cari file data")
        print("B. Data")
        print("C. Selesai")
        pilih = str(input("Pilih : "))
        print('-'*50)
        if (pilih == "A") or (pilih == "a"):
            cari = str(input("Masukan lokasi file : (contoh: e:\\__.txt) : "))
            myfile = open(cari,"r")
            myfile.close()
            print("\nFile ditemukan")
        elif (pilih == "B") or (pilih == "b"):
            while True:    
                myfile = open (cari,"r")
                teks = myfile.readlines()
                allDict = []
                for i in range (len(teks)):
                    dataOld = teks[i]
                    dataNew = dataOld.split('|')
                    Dictionary = {  "kode" : dataNew[0], 
                                    "nama" : dataNew[1], 
                                    "judul" : dataNew[2], 
                                    "tglPinjam" : dataNew[3],
                                    "tglPinjammax": dataNew[4]}
                    allDict += [Dictionary]
                find = str(input("Masukan kode member : "))
                for data in allDict:
                    if find == data["kode"]:
                        ada = True
                        break
                    else:
                        ada = False
                if (ada == True):
                    for data in allDict:
                        if find == data["kode"]:
                            tgl = data["tglPinjammax"]
                            tgal= tgl.split("-")
                            telat = diffDate(tgal)
                            denda = 2000 * telat
                            print("Data Peminjaman Buku")
                            print("Kode Member              : ",data["kode"])
                            print("Nama Member              : ",data["nama"])
                            print("Judul Buku               : ",data["judul"])
                            print("Tanggal Mulai Peminjaman : ",data["tglPinjam"])
                            print("Tanggal Maks. Peminjaman : ",data["tglPinjammax"])
                            print("Tanggal Pengembalian     : ",datetime.date(datetime.now()))
                            print("Terlambat                : ", telat,"hari")
                            print("Denda                    : ","Rp."+str(denda))
                            break
                
                elif (ada == False):
                    print("Data tidak ditemukan")
                    continue
                
                myfile.close()
                ulang = str(input("Lagi? (y/n) : "))
                if (ulang == "y") or (ulang == "Y"):
                    continue
                else:
                    break

        elif(pilih == "C") or (pilih == "c"):
            print('Terima Kasih')
            break

        else:
            print("\nPilih sesuai opsi yang tersedia")
    except NameError:
        print("\nAnda harus menemukan file text pada opsi A terlebih dahulu")
    except IndexError:
        print("\nNilai salah")
    except PermissionError:
        print("\nMasukan lokasi penyimpanan sesuai lokal disk yang tersedia dan jangan masukkan pada disk system.")
    except FileNotFoundError:
        print("\nDirektori penyimpanan tidak bisa ditemukan.")
    except ValueError:
        print("\nBilangan yang anda masukkan tidak valid")    