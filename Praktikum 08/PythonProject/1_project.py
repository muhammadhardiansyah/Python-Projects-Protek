n = int(input("Masukan berapa angka yang ingin anda olah ="))
myList = []
for i in range (n):
    i += 1
    print("Masukan angka ke", i," :", end=" ")
    x = int(input())
    myList = myList + [x]
myList.sort(reverse=True)
print(myList)