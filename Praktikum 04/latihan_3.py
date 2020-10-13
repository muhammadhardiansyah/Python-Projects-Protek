print("---Nomor 3---\n")
jarakAC = 795
bbm = 12
konsumsiBbm = 66.25
maks_tanki = 50
print("Diketahui:\n")
print("Jarak kota A dan kota C adalah:",jarakAC,"km")
print("jarak Konsumsi bbm setiap liter nya adalah:",bbm,"km")
print("Bbm yang diperlukan untuk perjalanan adalah:",konsumsiBbm,"liter")
print("Kapasitas tangki maksimal adalah =",maks_tanki,"liter")
print("\nPertanyaan:\nMinimal berapa kali pak Budi harus mengisi bensin hingga penuh supaya bisa menyelesaikan perjalanan?\nJawab:\n")

PomBensin = konsumsiBbm // maks_tanki

print("=",PomBensin,"kali")
print("\nJadi, Pak Budi harus mengisi bensin nya minimal",PomBensin, "kali untuk menyelesaikan perjalanan")
    
