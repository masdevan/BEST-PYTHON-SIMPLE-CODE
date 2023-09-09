# Membuat Daftar Nama dan menampilkannya namun dengan irisan pertama dan terakhir - Devan Yudistira Sugiharta

listTuple = ["Joko", "Gembul", "Supardi", "Yono", "Toni", "Waluyo"]

print("Nama Semula =====================================")
for listing in listTuple:
    print(listing)
    continue
print("Nama Yang Sudah DiIris ==========================")
for resListening in listTuple:
    hurufPertama = resListening[0]
    hurufTerakhir = resListening[-1]
    print(hurufPertama, hurufTerakhir)