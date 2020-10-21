#komputer memeilih random 0-100
#Tugas user menebak
#"Bilangan tebakan anda terlalu besar"
#"Bilangan tebakan anda terlalu kecil
from random import randint
print("="*12,"SELAMAT DATANG","="*12)
nama = input("Hai! Masukan nama anda :) :")
print("-"*40)
print("Halo",nama,"saya Mr. Jhon. Saya telah memilih bilangan bulat secara acak dari 0-100.")
siap = input("Kamu harus menebaknya.. Apakah kamu sudah siap? (y/n) :")
if (siap == 'y'):
    bil = randint (0,100)
    a = 0
    while True:
        print("Masukan tebakan anda, wahai",nama, end="")
        tebak = int(input(" :"))
        if (tebak < bil) and (tebak >= 0): 
            print("Tebakan anda terlalu kecil hai",nama,"!")
        elif (tebak > bil) and (tebak <= 100):
            print("Tebakan anda terlalu besar hai",nama,"!")
        elif (tebak < 0 ):
            print("Budayakan literasi, wahai",nama,".Rentangnya dimulai dari 0")
        elif (tebak > 100):
            print("Budayakan literasi ya ampun.. Rentangnya hanya sampai 100 wahai", nama,"!\n")
        elif (tebak == bil):
            break
        print("")
        a = a + 2
    nilai = 100 - a
    print("\nNice bruh! Jawaban anda benar.. Selamat",nama,"!")
    print("\nYour Score :",nilai,"\n")
else :
    print("\nBaiklah, mungkin lain kali.\n")