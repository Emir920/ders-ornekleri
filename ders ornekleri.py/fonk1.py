a = 5
ogrenci1 = {"ad": "Ali", "tc": "12345678901"}

print("ogrenci1:", ogrenci1,type(ogrenci1))

class Ogrenci():
    adi = "---"
    tc = "00000000000"

ogrenci2 = Ogrenci()

print(ogrenci2.adi)

ogrenci2.adi = "Emir"
print(" ogrenci2.adi:", ogrenci2.adi)

ogrenci3 = Ogrenci()
ogrenci3.adi = "Bartu"

print(" ogrenci3.adi:", ogrenci3.adi)
print("ogrenci3.tc:", ogrenci3.tc)

ogrenci3.tc = "98765432100"
print("ogrenci3.tc:", ogrenci3.tc)