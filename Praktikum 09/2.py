def bintang(n):
    for i in range (n):
        print(("*" * (1 + 2*i)).center(1 + 2*n))

try:
    n= int(input("Masukan n:"))
except ValueError:
    print("n harus bilangan bulat")
bintang(n)