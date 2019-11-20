import sqlite3
from os import system as komut

db = sqlite3.connect("kitaplar.sqlite")
imlec = db.cursor()


def result(sorgu):
    imlec.execute(sorgu)
    veriler = imlec.fetchall()
    for veri in veriler:
        print(veri)
    input("Ana menüye dönmek için enter'e basın")


menu = """
[1] Kitap Ara
[2] Yazar Ara
[Q] Çıkış
"""
while True:
    komut("cls")
    print(menu)

    islem = input("İşleminiz: ")

    if islem == "1":
        isim = input("Kitap Adı: ")
        sorgu = "SELECT * FROM kitaplik WHERE kitap='{}'".format(isim)
        result(sorgu)
    elif islem == "2":
        isim = input("Yazar Adı: ")
        sorgu = "SELECT * FROM kitaplik WHERE yazar='{}'".format(isim)
        result(sorgu)
    elif islem == "q" or islem == "Q":
        quit()
    else:
        print("Hatalı seçim")

db.close()
