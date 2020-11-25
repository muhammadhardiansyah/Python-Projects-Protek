#Buatlah func dataStat(x) 
#return value : [a,b,c]
#a adalah nilai rata- rata
#b adalah nilai maks
#c adalah nilai min
def dataStat(x):
    #rata-rata
    count = 0
    sum = 0
    for i in range (len(x)):
        sum = sum + x[i]
        count += 1
    a = sum / count
    #maks
    b = max(x)
    #minimal
    c = min(x)
    myList = [a,b,c]
    return print(myList)

n = int(input("Masukan berapa angka yang ingin anda olah ="))
myList = []
for i in range (n):
    i += 1
    print("Masukan angka ke", i," :", end=" ")
    x = int(input())
    myList += [x]
myTuple = tuple(myList)
dataStat(myTuple)