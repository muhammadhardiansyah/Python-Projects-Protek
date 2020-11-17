try:
    file = open("C:/myfile.txt","r")
    print(file.read())
except FileNotFoundError:
    print("Letak Direktori yang anda masukan salah")