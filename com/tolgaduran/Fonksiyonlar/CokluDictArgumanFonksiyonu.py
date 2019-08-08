# Çoklu dictionary kullanmak istediğimiz zamanlarda
# **kwargs parametresi ile istediğimiz kadar değişkeni kullanacağımız fonksiyon için tanımlayabiliriz
# Ancak tanımlama yapılırken <K,V> yani anahtar-değişken şeklinde yamamız gerekir.
# Bu durumda fonksiyonumuz dict type dizi olacaktır.
# Detaylı Bilgi İçin : https://www.fast.ai/2019/08/06/delegation/

def coklu(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


coklu(ad="Tolga", soyad="DURAN")
