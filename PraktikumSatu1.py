# Program Yang Meminta Pengguna Memasukkan Angka dan Mengidentifikasinya - Devan Yudistira Sugiharta
myInputer = input("Masukkan Angka dan Saya Akan Mengidentifikasinya : ")
isInput = int(myInputer)
if isInput == 0:
    print("Angka Nol")
elif isInput > 0:
    print("Angka Positif")
elif isInput < 0:
    print("Angka Negatif")
else:
    print("Kesalahan Input Program Terdeteksi")