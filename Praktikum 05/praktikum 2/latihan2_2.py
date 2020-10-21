i = 0
ganjil= 0
while True :
    i = i + 1
    if (i % 2 != 0):
        print(i)
        ganjil = ganjil + 1
    if (i >= 100):
        break
print("Banyaknya bilangan ganjil =", ganjil)