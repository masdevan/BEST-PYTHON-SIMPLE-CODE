# Meminta Pengguna Memasukkan Nama Produk, dan berapa Jumlah pembeliannya - Devan Yudistira Sugiharta
print("Selamat Datang di Toko Devan Yudistira Sugiharta, Silahkan Memilih Produk Kami!")
myList = {
    "Mangga" : 5000,
    "Pisang" : 3000,
    "Jeruk" : 2000,
    "Nangka" : 6000,
    "Apel" : 4000
}
for jenisBuah, Harga in myList.items():
    print(f"{jenisBuah} : {Harga}")

for Buah, HargaBuah in myList.items():
    buyer = input("Masukkan Apa yang Ingin Anda Beli, Contoh Mangga dan Ketik Batal untuk Membatalkan : ")
    if buyer == f"{Buah}":
        print(f"Harga Mangga Saat ini : {HargaBuah}")
        kart = int(f"{HargaBuah}")
        myBuy = input("Masukkan Jumlah Berapa Anda ingin Membelinya : ")
        forBuy = int(myBuy)
        Totals = kart * forBuy
        print("Total Belanjaan Anda Adalah : ", Totals)
        break
    elif buyer == "Batal":
        print("Permintaan Pesan Dibatalkan!")
        break
    else:
        print("Maaf Barang Yang Anda Cari Tidak Tersedia, Silahkan Memilih Barang Yang Lainnya!")
        break