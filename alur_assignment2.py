# Program While Memasukkan angka Positif dan Negatif Untuk Berhenti - Devan Yudistira Sugiharta
number = 0
while True:
    myInput = input("Masukkan angka bilangan bulat positif dan (Angka Bilangan Bulat Negatif Untuk Berhenti) : ")
    isInput = int(myInput)
    if isInput < 0:
        break
    else:
        number += isInput

print("Input Selesai dan berikut hasil inputan anda : ", number)
