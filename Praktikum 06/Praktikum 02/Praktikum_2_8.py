def luasSegitiga(a,t):
    luas = (a * t) / 2
    return luas

alas = 10
tinggi = 20
print("Luas segitiga dg alas",alas,"dan tinggi",tinggi,"adalah",luasSegitiga(alas,tinggi))
luasSegitiga1 = luasSegitiga(alas,tinggi)

alas = 15
tinggi = 45
print("Luas segitiga dg alas",alas,"dan tinggi",tinggi,"adalah",luasSegitiga(alas,tinggi))
luasSegitiga2 = luasSegitiga(alas,tinggi)

print("Jumlah luas kedua segitiga adalah",luasSegitiga1 + luasSegitiga2)