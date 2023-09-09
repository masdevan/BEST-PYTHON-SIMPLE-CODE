# Membuat Daftar Nama buah dan Attributnya dan izinkanlah orang meihat detailnya - Devan Yudistira Sugiharta
isArray = [
    ["Mangga", "Pisang", "Alpukat", "Nangka", "Manggis"],
    [3000, 4000, 5000, 6000, 7000],
    ["Kuning Tua", "Kuning Muda", "Hijau Tua", "Kuning", "Ungu"],
    ["Halus Besar", "Panjang Ramping", "Sedikit Kasar dan Besar", "Besar dan Berduri", "Bergelombang dan Menarik"]
]
print("List Buah : Mangga, Pisang, Alpukat, Nangka, Manggis")
myInputer = input("Masukkan Detail Buah apa Yang Ingin Anda Ketahui : ")
if myInputer == "Mangga":
    print("Nama Buah : ", isArray[0][0])
    print("Harga Buah : ", isArray[1][0])
    print("Warna Buah : ", isArray[2][0])
    print("Tekstur Buah : ", isArray[3][0])
elif myInputer == "Pisang":
    print("Nama Buah : ", isArray[0][1])
    print("Harga Buah : ", isArray[1][1])
    print("Warna Buah : ", isArray[2][1])
    print("Tekstur Buah : ", isArray[3][1])
elif myInputer == "Alpukat":
    print("Nama Buah : ", isArray[0][2])
    print("Harga Buah : ", isArray[1][2])
    print("Warna Buah : ", isArray[2][2])
    print("Tekstur Buah : ", isArray[3][2])
elif myInputer == "Nangka":
    print("Nama Buah : ", isArray[0][3])
    print("Harga Buah : ", isArray[1][3])
    print("Warna Buah : ", isArray[2][3])
    print("Tekstur Buah : ", isArray[3][3])
elif myInputer == "Manggis":
    print("Nama Buah : ", isArray[0][4])
    print("Harga Buah : ", isArray[1][4])
    print("Warna Buah : ", isArray[2][4])
    print("Tekstur Buah : ", isArray[3][4])
else:
    print("Inputan Anda Salah, Mohon Masukkan Input Salah Satu Seperti di List!")