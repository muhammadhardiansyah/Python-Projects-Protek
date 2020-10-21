from random import randint
a = 1
while True:
    bil = randint(0,10)
    print(bil)
    if bil == 5:
        break

    a = a + 1

print("Jumlah Perulangan :", a)