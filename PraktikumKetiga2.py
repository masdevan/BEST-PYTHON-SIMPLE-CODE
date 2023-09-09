# Permainan Tebak Angka Range 1-100 - Devan Yudistira Sugiharta
import random
mynum = random.randint(1, 100)
checkpoint = 5
print("Selamat Datang di Permainan Tebak Angka")
print("Dibuat Oleh Devan Yudistira Sugiharta")
while checkpoint > 0:
    myInput = input("Coba Anda Tebak Angka Berapa Yang Akan Keluar Mwehehe : ")
    inConv = int(myInput)

    if inConv > mynum:
        print("Maaf Angka Nya Kebesaran, Kecilin Lagi Ngab!")
    elif inConv < mynum:
        print("Maaf Angka Nya Kekecilan, Besarin Lagi Ngab!")
    elif inConv == mynum:
        print("Selamat Tebakan Anda Benar!")
        break

    checkpoint -= 1
    if checkpoint == 0:
        print("Maaf Kesempatan Anda habis, Coba Lagi Lain Kali hahaha!")
        break