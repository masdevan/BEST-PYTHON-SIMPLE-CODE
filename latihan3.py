# Buat Daftar Angka dari 1 - 10 dan tampilkan yang ganjil saja - Devan Yudistira Sugiharta
isAngka = [1,2,3,4,5,6,7,8,9,10]

isBlank = []
for angka in isAngka:
    if angka % 2 == 1:
        isBlank.append(angka)

print(isBlank)