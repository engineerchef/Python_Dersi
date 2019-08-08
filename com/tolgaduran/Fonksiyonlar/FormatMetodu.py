ad = input("Adınız : ")
soyad = input("Soyadınız : ")
yas = input("Yaşınız : ")

# Yukarıda kullanıcıdan girmesini istediğimiz ad, soyad ve yaş bilgilerine bağlı olarak normalde ekran çıktımızı
# print(ad + " " + soyad + " " + " " + yas + " yaşındadır.") şeklinde ifade ediyorduk.
# Ancak bunun yerine verilen değişkenlere bağlı olarak format() fonksiyonunu kullanarak print() fonksiyonu içerisinde
# tanımlayabileceğimiz gibi aşağıdaki şekilde de bir değişkene tanımlayarak da kullanabiliriz.

kullanici = "{} {} {} yaşındadır.".format(ad, soyad, yas)
print(kullanici)
