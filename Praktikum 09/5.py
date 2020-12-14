nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
 	     {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50}, 
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
	     {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print("="*50)
print("NIM".ljust(10), "NAMA".ljust(15), "N. MID".rjust(5), "N. UAS".rjust(10))
print("-"*50)
for data in nilai:
    print(data['nim'].ljust(10), data['nama'].ljust(15), str(data['mid']).rjust(5), str(data['uas']).rjust(10))