# Membuat program Yang memungkinkan Pengguna Memasukkan sebuah kata dan menghitung berapa kali kata tersebut muncul - Devan Yudistira Sugiharta
isBlank = []
hasclue = 0
while True:
    myInput = input("Masukkan Kosa Kata dan Kosongkan Program Untuk Berhenti : ") 
    isBlank.append(myInput)
    hasclue += 1

    if myInput == "":
        print("Kosa Kata Yang Anda Masukkan ============================")
        del isBlank[-1]
        for toarray in isBlank:
            print(toarray)
        print("Total Kosakata Yang Didapat =============================")
        print(hasclue - 1)
        break