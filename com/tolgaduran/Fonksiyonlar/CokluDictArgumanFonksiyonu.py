# Çoklu dictionary kullanmak istediğimiz zamanlarda
# **kwargs parametresi ile istediğimiz kadar değişkeni kullanacağımız fonksiyon için tanımlayabiliriz
# Ancak tanımlama yapılırken <K,V> yani anahtar-değişken şeklinde yamamız gerekir.
# Bu durumda fonksiyonumuz dict type dizi olacaktır

def coklu(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


coklu(ad="Tolga", soyad="DURAN")
