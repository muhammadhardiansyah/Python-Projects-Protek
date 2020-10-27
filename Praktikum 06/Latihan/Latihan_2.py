def starFormation1(n):
    for i in range(n):
        for j in range(i+1):
            print("* ",end=" ")
        print(" ")

starFormation1(4)

print("\n")

def starFormation2(n):
    for i in range(n):
        for j in range(n - i):
            print("* ",end=" ")
        print(" ")

starFormation2(4)

print("\n")

def starFormation(n):
    starFormation1(n//2)
    for i in range (n%2):
        for j in range((n//2)+1):
            print("* ",end=" ")
        print("")
    starFormation2(n//2)
                
       
starFormation(7)