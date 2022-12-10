a=int(input("sayı giriniz : "))
for i in range(2,a):
    if a%i==0:
        print("Girilen Sayı Asal Değildir.")
        break
    else:
        print("Girilen Sayı Asaldır.")
        break