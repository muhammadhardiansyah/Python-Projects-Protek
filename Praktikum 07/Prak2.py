#membuka dan mau membaca file F:/data.txt
try:
    file = open("F:/data.txt","r")

#baca baris pertama dari file
#simpan ke dalam variabel bil1 sebagai integer
    bil1 = int(file.readline())

#baca baris pertama dari file
#simpan ke dalam variabel bil2 sebgai integer
    bil2 = int(file.readline())

#hitung dan tampilkan hasil bagi
    hasil = bil1/bil2
    print(bil1,"dibagi",bil2,"sama dengan",hasil)

except FileNotFoundError:
    print("File tidak ditemukan")
except ZeroDivisionError:
    print("Tidak boleh pembagian nol")