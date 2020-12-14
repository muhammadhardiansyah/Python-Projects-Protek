def bintang(n):
    if (n % 2 != 0):
        x = n - 1
        a = int((0.5 * x) + 1)
        b = int((0.5 * x))
        for i in range (a):
            print(("*" * (1 + 2*i)).center(1 + 2*n))
        for i in range (b):
            i+=1
            print(("*" * (1 + 2*(b-i))).center(1 + 2*n))
    else:
        a = int(0.5 * n)
        b = int(0.5 * n)
        for i in range (a):
            print(("*" * (1 + 2*i)).center(1 + 2*n))
        for i in range (b):
            i+=1
            print(("*" * (1 + 2*(b-i))).center(1 + 2*n))
        

try:
    n= int(input("Masukan n:"))
except ValueError:
    print("n harus bilangan bulat")
bintang(n)