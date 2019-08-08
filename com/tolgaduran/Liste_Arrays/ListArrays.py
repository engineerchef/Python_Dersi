# Köşeli parantez içinde tanımlanır

listArray = ["elma", "armut", "şeftali"]

# ['elma', 'armut', 'şeftali'] çıktısını verir
print(listArray)

# şeftali çıktısını verir
print(listArray[2])

# dizinin 2nci indisindeki değeri değiştiriyoruz.
# ['elma', 'armut', 'karpuz'] çıktısını verir
listArray[2] = "karpuz"
print(listArray)

# dizi boyutunu verir => 3
print(len(listArray))

# diziye yeni bir değer ekliyruz
# # ['elma', 'armut', 'karpuz', 'muz'] çıktısını verir
listArray.append("muz")
print(listArray)

# dizinin 2nci indisine "kiraz" değerini atıyoruz
# ['elma', 'armut', 'kiraz', 'karpuz', 'muz'] çıktısını verir
listArray.insert(2, "kiraz")
print(listArray)

# belirlediğimiz değeri diziden çıkarıyoruz
# ['elma', 'armut', 'kiraz', 'muz']
listArray.remove("karpuz")
print(listArray)

# belirlenen indisteki değeri diziden siliyoruz
# ['elma', 'armut', 'muz'] çıktısını verir
listArray.pop(2)
print(listArray)

# indis belirtmediğimiz zaman dizinin son değerini siler
# ['elma', 'armut'] çıktısını verir
listArray.pop()
print(listArray)

# dizide belirtilen indisin değerini siler
# ['armut'] çıktısını verir
del listArray[0]
print(listArray)

# ayrıca del anahtarı herhangi bir indis belirtilmeden tüm diziye uygulanırsa listeyi tamamen siler
# liste tamamen silindiği için hata çıktısı döner
del listArray
print(listArray)

# clear() fonksiyonu dizinin içeriğini boşaltır
# [] çıktısını verir
listArray.clear()
print(listArray)

# önceden tanımlanmış olan dizinin birebir kopyasını alır
# ['elma', 'armut'] çıktısını verir
yeniListe = listArray.copy()
print(yeniListe)

# ayrıca kopyalama işlemi list() fonksiyonu ile de yapılabilir
baskaListe = list(listArray)
print(yeniListe)

# yeni bir liste dizisi list() fonsiyonu ile de tanımlanabilir
# NOT : İçiçe 2 tane parantez tanımlanmalıdır
listeSon = list(("Türkiye", "Almanya", "İsveç"))
print(listeSon)

# for döngüsü ile belirlenen dizinin içeriği liste halinde yazılabilir
for i in listeSon:
    print(i)

# if döngüsü ile dizide aranan değerin olup olmadığı kontrol edilebilir.
if "İsviçre" in listeSon:
    print("Ülke Bulundu!")
else:
    print("Ülke Bulunamadı!!!")

# Köşeli parantez içinde tanımlanır

listArray = ["elma", "armut", "şeftali"]

# ['elma', 'armut', 'şeftali'] çıktısını verir
print(listArray)

# şeftali çıktısını verir
print(listArray[2])

# dizinin 2nci indisindeki değeri değiştiriyoruz.
# ['elma', 'armut', 'karpuz'] çıktısını verir
listArray[2] = "karpuz"
print(listArray)

# dizi boyutunu verir => 3
print(len(listArray))

# diziye yeni bir değer ekliyruz
# # ['elma', 'armut', 'karpuz', 'muz'] çıktısını verir
listArray.append("muz")
print(listArray)

# dizinin 2nci indisine "kiraz" değerini atıyoruz
# ['elma', 'armut', 'kiraz', 'karpuz', 'muz'] çıktısını verir
listArray.insert(2, "kiraz")
print(listArray)

# belirlediğimiz değeri diziden çıkarıyoruz
# ['elma', 'armut', 'kiraz', 'muz']
listArray.remove("karpuz")
print(listArray)

# belirlenen indisteki değeri diziden siliyoruz
# ['elma', 'armut', 'muz'] çıktısını verir
listArray.pop(2)
print(listArray)

# indis belirtmediğimiz zaman dizinin son değerini siler
# ['elma', 'armut'] çıktısını verir
listArray.pop()
print(listArray)

# dizide belirtilen indisin değerini siler
# # ['armut'] çıktısını verir
# del listArray[0]
# print(listArray)

# ayrıca del anahtarı herhangi bir indis belirtilmeden tüm diziye uygulanırsa listeyi tamamen siler
# liste tamamen silindiği için hata çıktısı döner
# del listArray
# print(listArray)

# clear() fonksiyonu dizinin içeriğini boşaltır
# [] çıktısını verir
# listArray.clear()
# print(listArray)

# önceden tanımlanmış olan dizinin birebir kopyasını alır
# ['elma', 'armut'] çıktısını verir
yeniListe = listArray.copy()
print(yeniListe)

# ayrıca kopyalama işlemi list() fonksiyonu ile de yapılabilir
baskaListe = list(listArray)
print(yeniListe)

# yeni bir liste dizisi list() fonsiyonu ile de tanımlanabilir
# NOT : İçiçe 2 tane parantez tanımlanmalıdır
listeSon = list(("Türkiye", "Almanya", "İsveç"))
print(listeSon)

# for döngüsü ile belirlenen dizinin içeriği liste halinde yazılabilir
for i in listeSon:
    print(i)

# if döngüsü ile dizide aranan değerin olup olmadığı kontrol edilebilir.
if "İsviçre" in listeSon:
    print("Ülke Bulundu!")
else:
    print("Ülke Bulunamadı!!!")
