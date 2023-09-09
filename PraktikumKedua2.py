# Kalkulator Fahrenheit to Celcius - Devan Yudistira Sugiharta
myFahrenheit = input("Masukkan Jumlah Suhu Fahrenheit : ")
heitConv = int(myFahrenheit)
conv = (heitConv - 32) * 5 / 9
reStr = str(conv)
reSub = reStr[0:4]
print("Suhu Saat Ini berada di", reSub, "Derajat Celcius")