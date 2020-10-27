# a.	2 + 4 * 6 – 4
# b.	(4 + 7) * (6 - 9)
# c.	(10 + 2) / (7 + 5) / (12 - 34) 

from operation import*
print("A.",end=" ")
a = 2
b = 4
c = 6
d = 4
print(a,"+",b,"x",c,"-",d,"=",kurang(jumlah(kali(b,c),a),d))

print("B.",end=" ")
a = 4
b = 7
c = 6
d = 9
print("(",a,"+",b,") x (",c,"-",d,")=",kali(jumlah(a,b),kurang(c,d)))

print("C.",end=" ")
a = 10
b = 2
c = 7
d = 5
e = 12
f = 34
tambah1 = jumlah(a,b)
tambah2 = jumlah(c,d)
minus = kurang(e,f)
print("(",a,"+",b,") / (",c,"+",d,") / (",e,"-",f,") =", bagi(bagi(tambah1,tambah2),minus))