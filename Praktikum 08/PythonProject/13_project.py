def nilaiAkhir (mid,uas):
    hasil = (mid + (2 * uas)) / 3
    return hasil


def tertinggi (data):
    nilai2 = []
    for i in range (len(data)):
        dictionary = (data[i])
        nilai = nilaiAkhir(dictionary["mid"],dictionary["uas"])
        nilai2 += [nilai]
        highest = nilai2[0]
        for trtinggi in nilai2:
            if (trtinggi > highest):
                highest = trtinggi
            else:
                continue
        if (highest == nilai):
            nim = dictionary["nim"]
            nama = dictionary["nama"]
        else:
            continue
    hasil = print("Nilai akhir paling tinggi diperoleh oleh mahasiswa ber NIM",nim,"atas nama",nama)
    return hasil
        
    
        
        

nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80}, 	      
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},       
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, 
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30}, 
	        {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]

tertinggi(nilaiMhs)