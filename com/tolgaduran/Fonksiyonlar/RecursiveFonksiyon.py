# Recursion => kendisini çağırma özelliği
# Belirli bir düzende ilerleyen fonksiyonlar için kullanılır

# def tri_rec(value):
#     if value > 0:
#         result = value + tri_rec(value - 1)
#         print(result)
#     else:
#         result = 0
#     return result
#
#
# print("\n\nRecursion Örneği Sonuçları")
# tri_rec(6)


# faktöriyel
def fakt(deger):
    if deger == 1:
        return 1
    else:
        return deger * fakt(deger - 1)


print("Faktöriyel")
x = fakt(4)
print(x)


# verilen sayıdan 0'a kadar olan sayıların toplamı
def toplam(sayi):
    if sayi == 0:
        return 0
    else:
        return sayi + toplam(sayi - 1)


print("Toplam")
y = toplam(99)
print(y)


# Fibonacci
def fibo(deger):
    if deger == 0:
        return 0
    elif deger == 1:
        return 1
    else:
        return fibo(deger - 1) + fibo(deger - 2)


print("Fibonacci")
f = fibo(10)
print(f)
