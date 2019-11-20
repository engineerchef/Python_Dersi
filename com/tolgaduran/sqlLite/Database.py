import sqlite3

veriler = [("Ahmet Ümit", "İstanbul Hatırası"), ("Yaşar Kemal", "İnce Memed"), ("Paulo Coelho", "Simyacı"),
           ("Paulo Coelho", "Aldatmak")]
db = sqlite3.connect("kitaplar.sqlite")

imlec = db.cursor()
imlec.execute("CREATE TABLE IF NOT EXISTS kitaplik (yazar,kitap)")

for veri in veriler:
    imlec.execute("INSERT INTO kitaplik VALUES (?,?)", veri)

db.commit()
db.close()
