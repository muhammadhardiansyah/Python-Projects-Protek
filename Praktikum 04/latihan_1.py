#nomor 1
print("---NOMOR 1---\nDiketahui:")
tarif_jam = 12
tarif_awal = 200000
tarif_next = 10000
print("Tarif 12 jam pertama : Rp.",tarif_awal)
print("Tarif berikutnya : Rp.", tarif_next,"/jam")
jam_awal = 6
menit_awal = 0
jam_akhir = 23
menit_akhir = 50
menit = 60
print("Jam awal menyewa :jam",jam_awal," menit",menit_awal)
print("Jam akhir menyewa :jam",jam_akhir," menit",menit_akhir)
print("\nPertanyaan :\nTentukan tarif yang harus dibayarkan kepada rental mobil!\nJawab:")

#Menghitung lama waktu rental
jam_sewa = jam_akhir - jam_awal
menit_sewa = menit_akhir - menit_awal

print("Mobil dirental selama :",jam_sewa, "jam", menit_sewa, "menit")

#menghitung biaya rental
biaya = tarif_awal + ((jam_sewa - tarif_jam)*tarif_next) + ((menit_sewa/menit)*tarif_next)
print("Biaya yang harus dibayarkan:")
print("= Rp.",(biaya))
print("= Rp.",int(biaya))
print("\nJadi, total tarif yang harus dibayarkan kepada rental mobil adalah Rp.",int(biaya))