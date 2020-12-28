from datetime import datetime
from datetime import date
def diffDate(x):
    tglNew = date(year = int(x[0]), month = int(x[1]), day = int(x[2]))
    tglNow = datetime.date(datetime.now())
    selisih= tglNew - tglNow
    if ("days" in str(selisih)):
        selisihTgl= str(selisih).replace("days, 0:00:00","")
    elif ("day" in str(selisih)):
        selisihTgl= str(selisih).replace("day, 0:00:00","")
    else:
        selisihTgl=str(selisih).replace("0:00:00","0")
    hasil = int(selisihTgl)
    return hasil
try:
    tgl = input("Masukan tanggal (format: YYYY-MM-DD): ")
    tglsplit = tgl.split("-")
    if (diffDate(tglsplit) >= 0):
        print("\nSelisih dari hari ini menuju tanggal",tgl,"adalah",diffDate(tglsplit),"hari yang akan datang")
    else:
        jumlah = diffDate(tglsplit) - (2 * diffDate(tglsplit))
        print("\nSelisih dari hari ini menuju tanggal",tgl,"adalah",jumlah,"hari yang lalu")
except ValueError:
    print("Pastikan formt yang anda masukan sudah benar")