
def kuadrat (bil):
    kuadrat = 0
    hasil =[]
    for i in range (len(bil)):
        kuadrat = bil[i]**2
        hasil += [kuadrat]
    return print(hasil)

n = int(input("Masukan berapa angka yang ingin anda olah ="))
myList = []
for i in range (n):
    i += 1
    print("Masukan angka ke", i," :", end=" ")
    x = int(input())
    myList = myList + [x]
print(myList)
        
kuadrat(myList)