import sqlite3

db = sqlite3.connect("kitaplar.sqlite")
imlec = db.cursor()

imlec.execute("SELECT * FROM kitaplik")

# veriler = imlec.fetchall()
# for veri in veriler:
#     print(veri)

data=imlec.fetchmany(2)
for datas in data:
    print(datas)

db.close()
