try:
    n = int(input("Berapa nama mahasiswa yang ingin anda tulis? "))
    nama = []
    for i in range (n):
        masukan = input("Nama :")
        nama += [masukan]
    nama.sort()
    for i in range (len(nama)):
        print(nama[i],end=" ")
        print("(",len(nama[i]),"karakter )")

except ValueError:
    print("Input yang anda masukan salah")