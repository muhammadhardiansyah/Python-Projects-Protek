def isPrime(x):
    numb = 0
    for i in range (1,x):
        numb = x - i 
        if ( x % numb != 0):
            print(numb,"membagi habis",x,"?",False)
        if ( x % numb == 0):
            print(numb,"membagi habis",x,"?",True)
            break
    if ( numb == 1 ):
        print("Kesimpulan :",x,"Bilangan prima.")
    else :
        print("Kesimpulan :",x,"Bukan bilangan prima")

    
isPrime(7)

