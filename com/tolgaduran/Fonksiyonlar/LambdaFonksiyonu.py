# lambda fonksiyonu verilen değerlere göre işlem yapar ve tek bir tanımlık satırdan (statement) oluşur

sonuc = lambda a, b: a * b
print(sonuc(7, 4))


# lambda genellikle kısa süreli anonim fonksiyon oluşturmak istenildiğinde kullanılır
def fonk(sayi):
    return lambda a: a * sayi


ikiKat = fonk(2.5)
ucKat = fonk(3.5)

print(ikiKat(10))
print(ucKat(10))
