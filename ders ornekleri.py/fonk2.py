a = 5
ogretmen1 = {"ad": "Ali", "tc": "12345678901"}

print("ogretmen1:", ogretmen1,type(ogretmen1))

class Ogretmen():
    adi = "---"
    tc = "00000000000"

ogretmen2 = Ogretmen()

print(ogretmen2.adi)

ogretmen2.adi = "kemal hoca"
print(" ogretmen2.adi:", ogretmen2.adi)

ogretmen3 = Ogretmen()
ogretmen3.adi = "erdinc hoca"

print(" ogretmen3.adi:", ogretmen3.adi)
print("ogretmen3.tc:", ogretmen3.tc)

ogretmen3.tc = "98765432100"
print("ogretmen3.tc:", ogretmen3.tc)
