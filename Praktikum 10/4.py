myfile = open("e:\\Ardianprogram_2.txt","r")
teks = myfile.readlines()
allDict = []
for i in range (len(teks)):
    dataOld = teks[i]
    dataNew = dataOld.split("|")
    Dictionary = {"nim" : dataNew[0], "nama" : dataNew[1], "alamat" : dataNew[2]}
    allDict += [Dictionary]
cari = str(input("Masukan NIM yang mau dicari: "))
while True:
    #chek apakah ada nim tersebut di dalam Dict
    for data in allDict:
        if cari == data["nim"]:
            ada = True
            break
        else:
            ada = False
    #jika ada = True, cari dan print
    if ada == True :
        for data in allDict:
            if cari == data["nim"]:
                print("NIM      :",data["nim"])
                print("Nama     :",data["nama"])
                print("Alamat   :", data["alamat"])
                break
        break
    #jika ada = False, print(tidak ditemukan)
    elif ada == False:
        print("Data mahasiswa tidak ditemukan")
        break
print("-"*36)

myfile.close()