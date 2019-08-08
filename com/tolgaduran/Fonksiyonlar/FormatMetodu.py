ad = str(input("Adınız : "))
soyad = str(input("Soyadınız : "))
yas = int(input("Yaşınız : "))

# Yukarıda kullanıcıdan girmesini istediğimiz ad, soyad ve yaş bilgilerine bağlı olarak normalde ekran çıktımızı
# print(ad + " " + soyad + " " + " " + yas + " yaşındadır.") şeklinde ifade ediyorduk.
# Ancak bunun yerine verilen değişkenlere bağlı olarak format() fonksiyonunu kullanarak print() fonksiyonu içerisinde
# tanımlayabileceğimiz gibi aşağıdaki şekilde de bir değişkene tanımlayarak da kullanabiliriz.

kullanici = "{} {} {} yaşındadır.".format(ad, soyad, yas)
print(kullanici)

# İçerik belirleyerek de kullanıcı bilgilerini yaxdırabiliriz
kullanici = "{name} {surname} {age} yaşındadır.".format(name=ad, surname=soyad, age=yas)
print(kullanici)

# Veya içerik sırasını değiştirebiliriz
kullanici = "{1} {0} {2} yaşındadır.".format(ad, soyad, yas)
print(kullanici)

# Sağa yaslama işlemi
kullanici = "{:>15} {} {} yaşındadır.".format(ad, soyad, yas)
print(kullanici)

# Sola yaslama işlemi
kullanici = "{:<15} {} {} yaşındadır.".format(ad, soyad, yas)
print(kullanici)

# Ortalama işlemi
kullanici = "{:^15} {} {} yaşındadır.".format(ad, soyad, yas)
print(kullanici)

# Belirtilen yerlere belirtilen ifadelere uygun olacak şekilde string ve sayısal ifade gelmesi için
# :s => String
# :d => Sayısal
# belirteçleri kullanabiliriz.
kullanici = "{:s} {:s} {:d} yaşındadır.".format(ad, soyad, yas)
print(kullanici)

# Sayıları basamaklarına ayırmak için ise süslü parantezler arasında ayracı tanımlamamız yeterli olacaktır.
sayi=156875902154
print("Formatlanarak basamaklarına ayrılan sayı => {:,}".format(sayi))

# Bir de onluk sistemde verilen bir sayının ikilik sistemdeki karşılığını şu şeilde bulabiliriz.
print("648 sayısının ikilik sistemdeki karşılığı => {:b}".format(648))

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