try:
    file = open ("F:\\KULIAH\\Semester 1\\Pemrograman Terstruktur\\hello.txt")
    print("Isi file dari F:\\KULIAH\\Semester 1\\Pemrograman Terstruktur\\hello.txt adalah:")
    baris_1 = file.readline()
    baris_2 = file.readline()
    baris_3 = file.readline()
    print(baris_1+baris_2+baris_3)
except FileNotFoundError:
    print("File tidak ditemukan")
