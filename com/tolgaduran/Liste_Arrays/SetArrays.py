# Süslü parantez içinde tanımlanır

setArray = {"İsim", "Soyisim", "Doğum Yeri"}

# {'Soyisim', 'Doğum Yeri', 'İsim'} çıktısını verir
print(setArray)

# set dizileri sırasız (unordered) oldukları için rastgele sayılarlqa indislenirler
# sırasız olduğu için hata verir
print(setArray[2])

# set dizileri 1 kere oluşturulduktan sonra içeriği değişirilemez ancak ekleme veya çıkarma yapılabilir
# {'Doğum Yeri', 'İsim', 'Doğum Tarihi', 'Soyisim'} çıktısını verir
# her çıktı farklı sonuç verir
setArray.add("Doğum Tarihi")
print(setArray)

# birden fazla değer gireceksek update() fonksiyonunu kullanabiliriz
# normal parantez içinde köşeli parantez kullanmalıyız
# aksi halde girilen değerlerin her bir karakterini diziye ekler => setArray.update("Adres","TC No","Posta Kodu")
# setArray.update("Adres","TC No","Posta Kodu")
setArray.update(["Adres", "TC No", "Posta Kodu"])
print(setArray)

# dizi uzunluğu len() fonksiyonu ile tespit edilir
print(len(setArray))

# remove() fonksiyonu ile çıkarma yapılabilir
# çıkarılacak değer dizide bulunmuyorsa hata verir
# setArray.remove("Address")
setArray.remove("Adres")
print(setArray)

# remove() yerine discard() da kullanılabilir
# çıkarılacak değer dizide bulunmuyorsa hata vermez
# setArray.discard("Pst Kod")
setArray.discard("Posta Kodu")
print(setArray)

# pop() fonksiyonu sırasız tanımlanan set dizilerinde en son değeri diziden kaldırır
# unutmamak gerekir ki set dizileri sırasız olduğu için hangi değerin kaldırılacağı bilinemez.
x = setArray.pop()
print(x)

# clear() fonksiyonu dizideki tüm değerleri kaldırır
# set() çıktısını verir
setArray.clear()
print(setArray)

# diziyi tamamen siler
# dizi bulunamayacağı için hata döner
# NameError: name 'setArray' is not defined
del setArray
print(setArray)

# set dizisini set() fonksiyonu kullanarak da tanımlayabiliriz
# NOT : İçiçe 2 tane parantez tanımlanmalıdır
yeniSetArray = set(("Ülke", "Şehir", "İlçe"))
print(yeniSetArray)

# for döngüsü ile listeleyebiliriz
for a in yeniSetArray:
    print(a)

# if ile de içerik kontrolü yapabiliriz
if "Ülke" in yeniSetArray:
    print("Bulundu")
else:
    print("Bulunamadı")

# Süslü parantez içinde tanımlanır

setArray = {"İsim", "Soyisim", "Doğum Yeri"}

# {'Soyisim', 'Doğum Yeri', 'İsim'} çıktısını verir
print(setArray)

# set dizileri sırasız (unordered) oldukları için rastgele sayılarlqa indislenirler
# sırasız olduğu için hata verir
# print(setArray[2])

# set dizileri 1 kere oluşturulduktan sonra içeriği değişirilemez ancak ekleme veya çıkarma yapılabilir
# {'Doğum Yeri', 'İsim', 'Doğum Tarihi', 'Soyisim'} çıktısını verir
# her çıktı farklı sonuç verir
setArray.add("Doğum Tarihi")
print(setArray)

# birden fazla değer gireceksek update() fonksiyonunu kullanabiliriz
# normal parantez içinde köşeli parantez kullanmalıyız
# aksi halde girilen değerlerin her bir karakterini diziye ekler => setArray.update("Adres","TC No","Posta Kodu")
# setArray.update("Adres","TC No","Posta Kodu")
setArray.update(["Adres", "TC No", "Posta Kodu"])
print(setArray)

# dizi uzunluğu len() fonksiyonu ile tespit edilir
print(len(setArray))

# remove() fonksiyonu ile çıkarma yapılabilir
# çıkarılacak değer dizide bulunmuyorsa hata verir
# setArray.remove("Address")
setArray.remove("Adres")
print(setArray)

# remove() yerine discard() da kullanılabilir
# çıkarılacak değer dizide bulunmuyorsa hata vermez
# setArray.discard("Pst Kod")
setArray.discard("Posta Kodu")
print(setArray)

# pop() fonksiyonu sırasız tanımlanan set dizilerinde en son değeri diziden kaldırır
# unutmamak gerekir ki set dizileri sırasız olduğu için hangi değerin kaldırılacağı bilinemez.
x = setArray.pop()
print(x)

# clear() fonksiyonu dizideki tüm değerleri kaldırır
# set() çıktısını verir
setArray.clear()
print(setArray)

# diziyi tamamen siler
# dizi bulunamayacağı için hata döner
# NameError: name 'setArray' is not defined
# del setArray
# print(setArray)

# set dizisini set() fonksiyonu kullanarak da tanımlayabiliriz
# NOT : İçiçe 2 tane parantez tanımlanmalıdır
yeniSetArray = set(("Ülke", "Şehir", "İlçe"))
print(yeniSetArray)

# for döngüsü ile listeleyebiliriz
for a in yeniSetArray:
    print(a)

# if ile de içerik kontrolü yapabiliriz
if "Ülke" in yeniSetArray:
    print("Bulundu")
else:
    print("Bulunamadı")
