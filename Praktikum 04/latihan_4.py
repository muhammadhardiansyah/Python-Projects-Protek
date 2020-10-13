print("---Nomor 4---\n")
print("Diketahui:\n")
jarakAB = 125
kec_AB = 62
jarakBC =256
kec_BC = 70
print("Jarak kota A dan B =",jarakAB,"km")
print("Kecepatan rata-rata A -> B =",kec_AB,"km/jam")
print("Jarak kota B dan C =",jarakBC,"km")
print("Kecepatan rata rata B-> C =", kec_BC,"km/jam")
jam_awal = 6
menit_awal = 0
detik_awal = 0
jam_istirahat = 0
menit_istirahat = 45
detik_istirahat = 0
print("Pak Amir berangkat pada pukul =",jam_awal,".",menit_awal)
print("Istirahat di kota B selama =", menit_istirahat,"menit")
print("\nPertanyaan:\nPukul berapa pak Amir sampai di kota C?\nJawab:\n")

#waktu untuk A ke B
waktuAB = ((jarakAB*1000) / (kec_AB*1000/3600))
print("waktu yang dibutuhkan dari A ke B dalam satuan detik",int(waktuAB),"detik")
jam_AB = waktuAB // 3600
sisa_detik = waktuAB % 3600
menit_AB = sisa_detik // 60
sisa_detikAB = sisa_detik % 60
print("Dalam satuan jam adalah",int(jam_AB),"jam",int(menit_AB),"menit",int(sisa_detikAB),"detik\n")

#waktu untuk B ke C
waktuBC = ((jarakBC*1000) / (kec_BC*1000/3600))
print("waktu yang dibutuhkan dari B ke C dalam satuan detik",int(waktuBC),"detik")
jam_BC = waktuBC // 3600
sisa_detik = waktuBC % 3600
menit_BC = sisa_detik // 60
sisa_detikBC = sisa_detik % 60
print("Dalam satuan jam adalah",int(jam_BC),"jam",int(menit_BC),"menit",int(sisa_detikBC),"detik\n")

#penghitungan jam A ke B
jam_AkeB = jam_awal + jam_AB 
menit_AkeB = menit_awal + menit_AB 
detik_AkeB = detik_awal + sisa_detikAB
if (detik_AkeB > 60):
    menit_AkeB = menit_awal + menit_AB + 1
    detik_AkeB = (detik_awal + sisa_detikAB) % 60
if (menit_AkeB > 60):
    jam_AkeB = jam_awal + jam_AB  + 1
    menit_AkeB = (menit_awal + menit_AB) % 60
print("Pak Amir sampai di kota B pada jam",int(jam_AkeB),"lebih",int(menit_AkeB),"menit",int(detik_AkeB),"detik \n") 

#waktu istirahat di B
jam_diB = jam_AkeB + jam_istirahat
menit_diB = menit_AkeB + menit_istirahat
detik_diB = detik_AkeB + detik_istirahat
if (detik_diB > 60):
    menit_diB = menit_AkeB + menit_istirahat + 1
    detik_diB = (detik_AkeB + detik_istirahat) % 60
if (menit_diB > 60):
    jam_diB = jam_AkeB + jam_istirahat + 1
    menit_diB = (menit_AkeB + menit_istirahat) % 60
print("Pak Amir istirahat di kota B pada jam",int(jam_diB),"lebih",int(menit_diB),"menit",int(detik_diB),"detik \n") 

#Pak Amir sampai di C
jam_BkeC = jam_diB + jam_BC
menit_BkeC = menit_diB + menit_BC
detik_BkeC = detik_diB + sisa_detikBC
if (detik_BkeC > 60):
    menit_BkeC = menit_diB + menit_BC + 1
    detik_BkeC = (detik_diB + sisa_detikBC) % 60
if (menit_BkeC > 60):
    jam_BkeC = jam_diB + jam_BC + 1
    menit_BkeC = (menit_BkeC + menit_BC) % 60
print("Pak Amir sampai di kota C pada jam",int(jam_BkeC),"lebih",int(menit_BkeC),"menit",int(detik_BkeC),"detik \n")

print("Jadi, Pak Amir sampai di kota C pada jam",int(jam_BkeC),"lebih",int(menit_BkeC),"menit",int(detik_BkeC),"detik \n")

