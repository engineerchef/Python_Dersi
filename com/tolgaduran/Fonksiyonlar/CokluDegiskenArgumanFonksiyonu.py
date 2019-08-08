# Çoklu değişken tanımlayacağımız zamanlarda
# *args parametresi ile fonksiyon oluşturmamız fonksiyonun tekrarlabilirliği açısından oldukça önemlidir
# Bu tür bir fonksiyon tanımlamak istediğimizde içerik olarak her tür değişken tipini kullanabiliriz.

def coklu(*args):
    for i in args:
        print(i)


coklu(5, 5.9, 751, "Tolga", True)
