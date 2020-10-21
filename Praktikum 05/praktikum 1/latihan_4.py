kode = (input("Masukkan kode karyawan:"))
nama = input("Masukkan nama karyawan:")
golongan = input("Masukan golongan      :")

print("="*38)
print("STRUK RINCIAN GAJI KARYAWAN")
print("-"*38)

print("Nama Karyawan    :",nama, "(","Kode:",kode,")")
print("Golongan         :",golongan)
print("-"*38)

if (golongan == "A"): 
    GajiPokok = 10000000
    potongan = 2.5
elif (golongan == "B"): 
    GajiPokok = 8500000
    potongan = 2
elif (golongan == "C"): 
    GajiPokok = 7000000
    potongan = 1.5
elif (golongan == "D"): 
    GajiPokok = 5500000
    potongan = 1
else :
    GajiPokok = 0
    potongan = 0
terpotong = GajiPokok * (potongan/100)
GajiBersih = GajiPokok - terpotong

print("Gaji Pokok          :Rp.",GajiPokok)
print("Potongan (",potongan,"%)   :Rp.",int(terpotong))
print("-"*38,"-")
print("Gaji Bersih         :Rp.",int(GajiBersih))

if (GajiBersih == 0):
    print("\n","="*6, "PERINGATAN","="*6,"\n")
    print("Golongan yang anda masukan tidak valid")
    print("Golongan terdiri dari:\nA\nB\nC\nD")
