print("""
[1] Toplama İşlemi
[2] Çıkarma İşlemi
[3] Çarpma İşlemi
[4] Bölme İşlemi
[5] Üs Alma
[Q] Çıkış
""")

islem = input("İşlem Seçiniz : ")

if islem == "1":
    x = input("Birinci Sayı : ")
    y = input("İkinci Sayı : ")

    x = float(x)
    y = float(y)

    sonuc = x + y
    print("İşlem Sonucu : ", sonuc)

elif islem == "2":
    x = input("Birinci Sayı : ")
    y = input("İkinci Sayı : ")

    x = float(x)
    y = float(y)

    sonuc = x - y
    print("İşlem Sonucu : ", sonuc)

elif islem == "3":
    x = input("Birinci Sayı : ")
    y = input("İkinci Sayı : ")

    x = float(x)
    y = float(y)

    sonuc = x * y
    print("İşlem Sonucu : ", sonuc)

elif islem == "4":
    x = input("Birinci Sayı : ")
    y = input("İkinci Sayı : ")

    x = float(x)
    y = float(y)

    sonuc = x / y
    print("İşlem Sonucu : ", sonuc)

elif islem == "5":
    x = input("Taban : ")
    y = input("Kuvvet : ")

    x = float(x)
    y = float(y)

    sonuc = x ** y
    print("İşlem Sonucu : ", sonuc)

elif islem=="Q" or islem=="q":
    print("Çıkış Yapıldı!!!")
    exit()
else:
    print("Hatalı Giriş Yapıldı")
    exit()