try:
    path = str(input("Masukan nama file           :"))
    file = open(path,"a")

    while True:
        Data = input("Data yang mau anda tambahkan:") 
        file.write(Data)
        lagi = input("Anda ingin menambahkan data lagi? (y/n) :")
        if (lagi == 'y'):
            continue
        else :
            break 

    file.close()
except PermissionError:
    print("Direktori tidak bisa diakses")
except FileNotFoundError:
    print("Direktori tidak ada")
except OSError:
    print("Data yang anda masukan tidak valid")