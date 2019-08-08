# Parametresiz fonksiyon
def fonk():
    print("Merhaba Dünya!")


fonk()


# Parametreli fonksiyon
def parafonk(name):
    print("Merhaba " + name)


parafonk("Tolga")


# Ön tanımlı parametreli fonksiyon
def ulke(country="Turkey"):
    print("I am from " + country)


ulke()
ulke("Sweden")


# listeler için fonksiyon oluşturma
def listfonk(fruit):
    for i in fruit:
        print(i)


meyve = ["elma", "armut", "şeftali"]
listfonk(meyve)


# return değer döndüren fonksiyon
# bu fonksiyonda return yerine yield kullanılamaz
# yield generator (üreteç) yapılarında kullanılır
def returnfonk(value):
    return 5 * value


print(returnfonk(3))
