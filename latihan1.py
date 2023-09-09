# Program Input Nama Masukkan ke daftar dan urutkan dengan alfabetik - Devan Yudistira Sugiharta
blankName = []
while True:
    myInput = input("Masukkan Nama Anda, Bebas, Dan saya Akan Membuatkan data List nya / Ketikkan 'end' Untuk Mengakhiri Program : ")

    if myInput:
        blankName.append(myInput)
    elif myInput == "end":
        print("Program Selesai Dijalankan")
        break

    for i, myInput in enumerate(blankName, start=1):
        print(f"{i} {myInput}")