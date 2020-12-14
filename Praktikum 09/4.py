import random
def shuffleString(x,n):
    lisGabung = []
    i = 0
    while True:
        i+=1
        a = (random.sample(x,len(x)))
        gabung="".join(a)
        if (gabung in lisGabung):
            i-=1
        else:
            lisGabung += [gabung]
        if (i == n):
            break
    return print(lisGabung)
        



shuffleString("aku",3)