a = [1,5,6,3,6,9,11,20,12]
b = [7,4,5,6,7,1,12,5,9]
#sisipkan nilai 10 ke indeks 3 dari a
a.insert(3, 10)
#sisipkan nilai 15 ke indeks 2 dari b
b.insert(2, 15)

#sisipkan nilai 4 ke indeks terakhir dari a
a.append(4)
#sisipkan nilai 8 ke indeks terakhir dari b
b.append(8)

#Sorting secara ascending pada list a dan b
a.sort()
b.sort()

#sublist dari a (mulai dari indeks ke 0 s/d 7)
c = a[0:8]
#sublist dari b (mulai indeks ke 2 s/d 9)
d = b[2:10]

#list e elemennya  hasil penjumlahan setiap elemen c dan d 
e = []
for i in range (len(c)):
    jumlah = c[i] + d[i]
    e = e + [jumlah]

#ubah list e ke dalam tuple
e = tuple(e)
print(e)

#cari nilai min
print("nilai min = ",min(e))
#maks
print("nilai maks = ",max(e))
#jumlah
print("jumlah seluruh nilai e = ",sum(e))

         
