class SaglikDurumu:
    """Sağlık durumu sınıfı"""
    
    def __init__(self, ad, yas, kilo, boy):
        self.ad = ad
        self.yas = yas
        self.kilo = kilo
        self.boy = boy
    
    def bmi(self):
        """BMI hesapla"""
        return round(self.kilo / (self.boy / 100) ** 2, 2)
    
    def kategori(self):
        """Sağlık kategorisi"""
        bmi = self.bmi()
        if bmi < 18.5:
            return "Zayıf"
        elif bmi < 25:
            return "Normal"
        elif bmi < 30:
            return "Fazla Kilolu"
        else:
            return "Obez"
    
    def bilgi(self):
        """Sağlık bilgilerini göster"""
        print(f"Ad: {self.ad}")
        print(f"Yaş: {self.yas}")
        print(f"BMI: {self.bmi()} - {self.kategori()}")

kisi = SaglikDurumu("Emir", 12, 80, 180)
kisi.bilgi()