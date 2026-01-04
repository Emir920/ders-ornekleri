class Ilan:
    def __init__(self,a,b,c):
        self.no = a
        self.baslik = b
        self.aciklama = c

    def bilgiVer(self):
        return f"ilan no: {self.no}, ilan basligi: {self.baslik}, ilan aciklamasi: {self.aciklama}"
    
class EvIlani(Ilan):
    def __init__(self,a,b,c,d):
        super().__init__(a,b,c)
        self.oda_sayisi = d

    def bilgiVer(self):
        return f"{super().bilgiVer()}, oda sayisi: {self.oda_sayisi}"
Ilan1 = Ilan(1001,"Satilik Araba","Temiz kullanilmis satilik araba.")

Ilan2 = Ilan(1002,"Kiralik Daire","Merkezi konumda kiralik daire.")

print("\nIlan1 Bilgileri:", "ilan no:", Ilan1.no, "ilan basligi:", Ilan1.baslik, "ilan aciklamasi:", Ilan1.aciklama)
print("\nIlan2 Bilgileri:", "ilan no:", Ilan2.no, "ilan basligi:", Ilan2.baslik, "ilan aciklamasi:", Ilan2.aciklama)

print(Ilan1.bilgiVer())
print(Ilan2.bilgiVer())

Ilan3 = EvIlani(2001,"Kiralik Ev","Deniz manzarali kiralik ev.",3)
print("\nIlan3 Bilgileri:", "ilan no:", Ilan3.no, "ilan basligi:", Ilan3.baslik, "ilan aciklamasi:", Ilan3.aciklama, "oda sayisi:", Ilan3.oda_sayisi)
print(Ilan3.bilgiVer())