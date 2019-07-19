print("""
+   => Toplama
-   => Çıkarma
*   => Çarpma
/   => Bölme
//  => Taban Bölme
%   => Mod Alma
""")

x = int(input("Birinci Sayı\t: "))
# y = float(input("İkinci Sayı\t: "))
#
# toplam = x + y
# fark = x - y
# carpim = x * y
# bolum = x / y
# taban = x // y
#
# print("Toplam\t\t:", toplam)
# print("Fark\t\t:", fark)
# print("Çarpım\t\t:", carpim)
# print("Bölüm\t\t:", bolum)
# print("Taban Bölme\t:", taban)

if x % 2 == 0:
    print("Sayı Çift")
else:
    print("Sayı Tek")
