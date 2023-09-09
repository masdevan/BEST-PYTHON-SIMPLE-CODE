# Kalkulator BMI (Body Mass Index) - Devan Yudistira Sugiharta
print("Selamat Datang di Kalkulator BMI (Body Mass Index)")
myMass = input("Masukkan Berat Badan Anda contoh (50): ")
conMass = int(myMass)
myTall = input("Masukkan Tinggi Badan Anda dalam Meter, contoh (1.6) : ")
conTall = float(myTall)
maxTotal = conMass / (conTall * conTall)
isString = str(maxTotal)
isTotal = isString[0:4]
if maxTotal < 18.5:
    print("Total BMI Anda Adalah", isTotal, "(Underweight)")
elif 18.5 <= maxTotal <= 24.9:
    print("Total BMI Anda Adalah", isTotal, "(Normal)")
elif 25 <= maxTotal <= 29.9:
    print("Total BMI Anda Adalah", isTotal, "(Overweight)")
elif maxTotal > 30:
    print("Total BMI Anda Adalah", isTotal, "(Obesitas)")
else:
    print("BMI Tidak Diketahui, Ulangi Menginput Data!")