# Normal parantez ile tanımlanır

tupleArray = ("elma", "armut", "muz")

# ('elma', 'armut', 'muz') çıktısını verir
print(tupleArray)

# 1inci indisin değerini verir => armut
print(tupleArray[1])

# for döngüsü ile demet içerisindeki değerler listelenebilir
for x in tupleArray:
    print(x)

# if döngüsü ile demet içerisinde aranan değerin olup olmadığı tespit edilebilr
if "muz" in tupleArray:
    print("Meyve Bulundu")
else:
    print("Meyve Bulunamadı!!!")

# len() fonksiyonu ile demet boyutu tespit edilir
print(len(tupleArray))

# demetlerde del, remove ve add işlemleri yapılamaz.

# yeni bir demet oluşturma işlemi tuple() fonksiyonu ile de tanımlanabilir
# NOT : İçiçe 2 tane parantez tanımlanmalıdır
yeniTuple = tuple(("Ülke", "Şehir", "Mahalle"))
print(yeniTuple)

# Normal parantez ile tanımlanır

tupleArray = ("elma", "armut", "muz")

# ('elma', 'armut', 'muz') çıktısını verir
print(tupleArray)

# 1inci indisin değerini verir => armut
print(tupleArray[1])

# for döngüsü ile demet içerisindeki değerler listelenebilir
for x in tupleArray:
    print(x)

# if döngüsü ile demet içerisinde aranan değerin olup olmadığı tespit edilebilr
if "muz" in tupleArray:
    print("Meyve Bulundu")
else:
    print("Meyve Bulunamadı!!!")

# len() fonksiyonu ile demet boyutu tespit edilir
print(len(tupleArray))

# demetlerde del, remove ve add işlemleri yapılamaz.

# yeni bir demet oluşturma işlemi tuple() fonksiyonu ile de tanımlanabilir
# NOT : İçiçe 2 tane parantez tanımlanmalıdır
yeniTuple = tuple(("Ülke", "Şehir", "Mahalle"))
print(yeniTuple)
