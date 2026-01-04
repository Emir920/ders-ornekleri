class Dusman:
    def __init__(self,ad,can,guc):
        self.ad = ad
        self.can = can
        self.guc = guc

    def saldir(self,hedef):
        hedef.can -= self.guc
        return f"{self.ad} {hedef.ad} 'a {self.guc} hasar verdi. Kalan can: {hedef.can}"

class DusmanUyarisi(Dusman):
    def __init__(self,ad,can,guc,uyari_seviyesi):
        super().__init__(ad,can,guc)
        self.uyari_seviyesi = uyari_seviyesi
Dusman1 = Dusman("Ork",100,15)
Dusman2 = Dusman("Goblin",80,10)
print("\nDusman1 Bilgileri:", "Ad:", Dusman1.ad, "Can:", Dusman1.can, "Guc:", Dusman1.guc)
print("\nDusman2 Bilgileri:", "Ad:", Dusman2.ad, "Can:", Dusman2.can, "Guc:", Dusman2.guc)
Dusman3 = Dusman("Troll",150,20)
print("\nDusman3 Bilgileri:", "Ad:", Dusman3.ad, "Can:", Dusman3.can, "Guc:", Dusman3.guc)

print(Dusman1.saldir(Dusman2))
print(Dusman2.saldir(Dusman1))
print(Dusman3.saldir(Dusman1))
Dusman4 = DusmanUyarisi("Ejderha",300,50,"Yuksek")
print("\nDusman4 Bilgileri:", "Ad:", Dusman4.ad, "Can:", Dusman4.can, "Guc:", Dusman4.guc, "Uyari Seviyesi:", Dusman4.uyari_seviyesi)
print(Dusman4.saldir(Dusman1))