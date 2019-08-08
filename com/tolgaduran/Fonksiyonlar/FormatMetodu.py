ad = input("Adınız : ")
soyad = input("Soyadınız : ")
yas = input("Yaşınız : ")

# Yukarıda kullanıcıdan girmesini istediğimiz ad, soyad ve yaş bilgilerine bağlı olarak normalde ekran çıktımızı
# print(ad + " " + soyad + " " + " " + yas + " yaşındadır.") şeklinde ifade ediyorduk.
# Ancak bunun yerine verilen değişkenlere bağlı olarak format() fonksiyonunu kullanarak print() fonksiyonu içerisinde
# tanımlayabileceğimiz gibi aşağıdaki şekilde de bir değişkene tanımlayarak da kullanabiliriz.

kullanici = "{} {} {} yaşındadır.".format(ad, soyad, yas)
print(kullanici)

# Benzer şekilde aşağıdaki örnekte olduğu gibi verilen bir hark dizisindeki her harfi ayrı ayrı yazdırmak için
# for döngüsünü kullanarak formatlama işlemini fonksiyon kullanarak yapalım.
harfler = "abcçdefgğhıijklmnoöpqrsştuüvwxyz"
print("\nHarflerin format() fonskiyonu kullanılarak sırayla yazılışı\n")


def harfFonksiyonu():
    for i in harfler:
        print("Harf : {}".format(i))


harfFonksiyonu()


# Ya da Listeler kullanılarak da dizi içerisindekileri şu şekilde yazdırabiliriz
def listeFonksiyonu(*args):
    for i in args:
        print("İçerik : {}".format(i))


print("\nListe içerik\n")
listeFonksiyonu("Tolga", "DURAN", 38)
