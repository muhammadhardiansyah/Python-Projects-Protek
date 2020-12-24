myfile = open("e:\\Ardianprogram_2.txt","r")
teks = myfile.readlines()
allDict = []
for i in range (len(teks)):
    dataOld = teks[i]
    dataNew = dataOld.split("|")
    Dictionary = {"nim" : dataNew[0], "nama" : dataNew[1], "alamat" : dataNew[2]}
    allDict += [Dictionary]
print("dataMhs = ", allDict)

myfile.close()