def faktoriall(angka):
    x = 1
    for i in range(angka):
        i = i+1
        x = x * i
    hsil = x
    return hsil

def faktorial (a,n,r):
    if (a == 'P'):
        hasil = faktoriall(n) / faktoriall (n -r)
        print(a,"(",n,",",r,") = ",(hasil))
    elif (a == 'C'):
        hasil = faktoriall(n) / ( faktoriall(r) * faktoriall(n-r) )
        print(a,"(",n,",",r,") = ",(hasil))
    else :
        print(" Masukan anda salah, masukan seperti ini : faktorial('P atau C',angka,angka)")

print("A. ",end=" ")
faktorial("C",5,3)

print("B. ",end=" ")
faktorial("P",10,7)