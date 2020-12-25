allNim = []
allNama = []
allAlamat = []
a = 0
while True:
    nim     = str(input("Masukan NIM      : "))
    nama    = str(input("Masukan Nama Mhs : "))
    alamat  = str(input("Masukan Alamat   : "))
    print("-"*30)
    allNim += [nim]
    allNama += [nama]
    allAlamat += [alamat]
    
    ulang   = str(input("Masukan input lagi? (y/n) : "))
    if (ulang == "y"):
        continue
    else:
        break
    a += 1

myfile = open("e:\\Ardianprogram_2.txt","w") 
for i in range (len(allNim)):
    a=(allNim[i]+"|"+allNama[i]+"|"+allAlamat[i])
    myfile.write(a)
    myfile.write("\n")
myfile.close()
print("\nSukses!\nPergi ke e:\\Ardianprogram_2.txt untuk melihat hasilnya.\n")



