#Nilai akhir diperoleh dari rumus (Nilai MID + 2 Nilai UAS)/3
#Status nantinya hanya terdiri dari LULUS atau TIDAK LULUS. Dikatakan statusnya LULUS jika Nilai Akhirnya lebih atau sama dengan 60. 
#Sedangkan jika kurang dari 60 maka TIDAK LULUS

nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	     {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	     {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print("="*70)
print("NIM".ljust(10), "NAMA".ljust(15), "N. MID".rjust(5), "N. UAS".rjust(10), "N.AKHIR".rjust(10), "STATUS".rjust(10))
print("-"*70)
for data in nilai:
    nilaiAkhir = int((data["mid"] + 2 * data["uas"])/3)
    if (nilaiAkhir >= 60):
        status = "LULUS"
    else:
        status = "TIDAK LULUS"
    print(data['nim'].ljust(10), data['nama'].ljust(15), str(data['mid']).rjust(5), str(data['uas']).rjust(10), str(nilaiAkhir).rjust(10), status.rjust(10))
print("-"*70)