print("-"*30)
print("PROGRAM HITUNG RATA-RATA")
print("-"*30)
tmbh = 0
n = 0
while True:
    try:
        a = int(input("Masukan bilangan bulat: "))
    except ValueError:
            print("Angka bukan bilangan bulat")
            continue
    tmbh += a
    n += 1
    lagi = input("Lagi (y/n) ? ")
    if (lagi == 'y'):
        continue
    else:
        break
print("-"*30)
hasil = tmbh / n
print("Rata-ratanya adalah :",hasil)
