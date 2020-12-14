mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']
print("="*70)
print("NIM".ljust(8),"NAMA MAHASISWA".ljust(20), "TGL LAHIR".ljust(20), "TEMPAT LAHIR")
print("-"*70)
for i in mhs:
    data = i.split(":")
    tgl = data[2].split("-")
    print(data[0].ljust(8), data[1].ljust(20), str(tgl[2])+"/"+str(tgl[1])+"/"+str(tgl[0]).ljust(14), data[3])
print("-"*70)