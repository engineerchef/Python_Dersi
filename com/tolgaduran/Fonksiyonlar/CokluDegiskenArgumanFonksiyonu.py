# Çoklu değişken tanımlayacağımız zamanlarda
# *args parametresi ile fonksiyon oluşturmamız fonksiyonun tekrarlabilirliği açısından oldukça önemlidir
# Bu tür bir fonksiyon tanımlamak istediğimizde içerik olarak her tür değişken tipini kullanabiliriz.
# Detaylı Bilgi İçin : https://www.fast.ai/2019/08/06/delegation/

def coklu(*args):
    for i in args:
        print(i)


coklu(5, 5.9, 751, "Tolga", True)
