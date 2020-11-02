def sqNumbers (a,b):
    i = 0
    for numb in range (a , b):
       for i in range (b):
           if (numb == i**2):
               print (numb)
sqNumbers(10,50)