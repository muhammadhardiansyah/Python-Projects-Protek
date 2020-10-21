kode = (input("Masukkan kode karyawan:"))
nama = input("Masukkan nama karyawan:")
golongan = input("Masukan golongan      :")
status = int(input("Masukkan status (1: menikah, 2: blm):"))
if (status == 1):
    anak = int(input("Masukkan jumlah anak   :"))

print("="*38)
print("STRUK RINCIAN GAJI KARYAWAN")
print("-"*38)

print("Nama Karyawan    :",nama, "(","Kode:",kode,")")
print("Golongan         :",golongan)
if (status == 1):
    print("Status menikah   : Menikah")
    print("Jumlah Anak      :",anak)
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

ptonganNikah = 10
ptonganAnak = 5 
terpotong = GajiPokok * (potongan/100)
if (status == 1):
    tunjnganNikah = GajiPokok * (ptonganNikah/100)
    tunjnganAnak = (GajiPokok * (ptonganAnak/100))*anak
    GajiKotor =  GajiPokok+ tunjnganNikah + tunjnganAnak
    GajiBersih = GajiKotor - terpotong
else :
    GajiBersih = GajiPokok - terpotong

print("Gaji Pokok           :Rp.",GajiPokok)
if (status == 1):
    print("Tunjangan Istri/Suami:Rp.",int(tunjnganNikah))
    print("Tunjangan Anak       :Rp.",int(tunjnganAnak))
    print("-"*38,"+")
    print("Gaji Kotor           :Rp.",int(GajiKotor))
print("Potongan (",potongan,"%)    :Rp.",int(terpotong))
print("-"*38,"-")
print("Gaji Bersih          :Rp.",int(GajiBersih))
