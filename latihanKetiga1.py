# Program Pengguna memasukkan daftar nama lalu meletakannya pada sebuah set lalu menampilkannya - Devan Yudistira Sugiharta
isSet = input("Masukkan Nama Daftar Nama Yang Ingin Anda Input : ")
splitter = isSet.split()
isBlank = set(splitter)

print("Daftar Nama")
for snap in isBlank:
    print(snap)