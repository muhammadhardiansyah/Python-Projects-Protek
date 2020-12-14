def ubahHurufreplace (teks, a, b):
    teksBaru = teks.replace(a,b)
    return print(teksBaru)

ubahHurufreplace("matematika", "t", "s")

def ubahHuruflooping (teks, a, b):
    m = 0
    n = 1
    lis_huruf= []
    while True:
        huruf = teks[m:n]
        if (huruf == a):
            huruf = b
        else:
            huruf = huruf
        lis_huruf += [huruf]
        m += 1
        n += 1
        if (len(teks) == m):
            break
    gabung = "".join(lis_huruf)
    return print(gabung)
ubahHuruflooping("matematika","t","s")