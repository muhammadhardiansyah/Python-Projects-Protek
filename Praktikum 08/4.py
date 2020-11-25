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
print(a)
b.sort()
print(b)