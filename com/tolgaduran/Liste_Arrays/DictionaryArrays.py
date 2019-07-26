# Süslü parantez içinde tanımlanır
# <K,V> mantığı ile anahtar-değer çiftleri ile çalışır
# indis değeri olarak anahtar kullanılır

dictionaryArray = {
    "marka": "Ford",
    "model": "Mustang",
    "renk": "Turuncu",
    "yıl": 2018
}
# {'marka': 'Ford', 'model': 'Mustang', 'yıl': '2019'} çıktısını verir
print(dictionaryArray)

# belirtilen anahtara karşılık gelen değeri verir
# Mustang çıktısını verir
print(dictionaryArray["model"])

# sadece anahtar kullanmak yerine get() fonksiyonu ile de değer alınabilir
x = dictionaryArray.get("model")
print(x)

# anahtara bağlı olarak içerik değiştirilebilir
dictionaryArray["model"] = "Mustang GT"
dictionaryArray["yıl"] = 2019
print(dictionaryArray)

# for döngüsü ile hem anahtar hem de değerler alınabilir
# 1. anahtarların alınması
for x in dictionaryArray:
    print(x)
# 2. değerlerin alınması
for y in dictionaryArray:
    print(dictionaryArray[y])

# bunlara ek olarak items() fonksiyonu kullanılarak da <K,V> değerleri birlikte alınabilir
for a, b in dictionaryArray.items():
    print(a, "\t: ", b)

# if ile anahtar değeri kontrol edilebilir
if "model" in dictionaryArray:
    print("'model' anahtarı dizide bulunmaktadır")
else:
    print("'model' anahtarı dizide bulunamadı!!!")

# len() fonksiyonu ile dizi boyu tespit edilebilir
print(len(dictionaryArray))

# pop() fonksiyonu belirtilen anahtar-değer çiftini siler
x = dictionaryArray.pop("yıl")
print(x)
print(dictionaryArray)

# popitem() fomksiyonu dizideki son <K,V> çiftini kaldırır
# NOT : Python 3.7'den önceki sürümlerde rastgele <K,V> çifti kaldırır
y = dictionaryArray.popitem()
print(y)
print(dictionaryArray)

# del ile pop() arasındaki tek fark
# del sonrası herhangi bir değer dönmez
# pop() sonrasında silinecek değeri görebiliriz ve değer dönmüş olur
del dictionaryArray["marka"]
print(dictionaryArray)

# del ile diziyi tamamen silebiliriz
# hata verir
# NameError: name 'dictionaryArray' is not defined
# del dictionaryArray
# print(dictionaryArray)

# clear() fonksiyonu ile dizi içeriği tamamen silinir
dictionaryArray.clear()
print(dictionaryArray)

# dict() fonksiyonu ile de ddictionary dizisi tanımlayabiliriz
# NOT : dict() ile dizi tanımlanırken anahtar değerleri tırmak içinde yazılmaz
yeniDictDizisi = dict(marka="Ford", model="Mustang GT", yıl=2019)
print(yeniDictDizisi)

# copy() fonksiyonu ile kopyalama yapabiliriz
newDict = yeniDictDizisi.copy()
print(newDict)

# dict() fonksiyonu ile de kopyalama yapılabilir
sonDict = dict(yeniDictDizisi)
print(sonDict)
