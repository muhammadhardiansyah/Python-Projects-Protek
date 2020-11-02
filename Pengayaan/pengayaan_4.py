#untuk biner dalam 8 bit
def bin2dec (n):
    b8 = str(n)[:1]
    b7 = str(n)[1:2]
    b6 = str(n)[2:3]
    b5 = str(n)[3:4]
    b4 = str(n)[4:5]
    b3 = str(n)[5:6]
    b2 = str(n)[6:7]
    b1 = str(n)[7:8]
    
    des = (int(b1)* 2**0) + (int(b2)* 2**1) + (int(b3)* 2**2) + (int(b4)* 2**3) + (int(b5)* 2**4) + (int(b6)* 2**5) + (int(b7)* 2**6) + (int(b8)* 2**7)
    hasil = print(des)
    return hasil 
bin2dec(10000000)