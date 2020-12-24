myfile = open("e:\\Ardianprogram_1.txt","w")
myfile.write("100\n102\n99\n89\n192\n938\n107\n241\n")
myfile.close()

myfile = open("e:\\Ardianprogram_1.txt","r")
angka = myfile.readlines()
i = 0
genap = 0
ganjil = 0

try:
    while True:
        value = int(angka[i])
        if (value % 2 == 0):
            genap += 1
        if (value % 2 != 0):
            ganjil += 1
        i += 1

        if not angka:
            break
except IndexError:
    print("HASIL : ")
print("Banyaknya bilangan genap     :",genap)
print("Banyaknya bilangan ganjil    :",ganjil)

myfile.close()