bina = int(input("Masukkan nilai Bhs Indonesia :"))
ipa = int(input("Masukan nilai IPA :"))
mtk = int(input("Masukan nilai matematika :"))


if (bina >= 60) and (bina <= 100):
    if (ipa >= 60) and (ipa <=100):
        if (mtk >= 70) and (mtk <= 100):
            hasil = "LULUS"
        elif (mtk < 70) and (mtk >= 0):
            hasil = 'TIDAK LULUS'
    elif (ipa < 60) and (ipa >= 0):
        hasil = 'TIDAK LULUS'
elif (bina < 60) and (bina >= 0):
    hasil = "TIDAK LULUS"


print("Hasil kelulusan :", hasil)
