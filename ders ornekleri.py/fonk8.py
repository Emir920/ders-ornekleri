class Hesap:
    def __init__(self, sifre, bakiye=0):
        self.sifre = sifre
        self.__bakiye = bakiye

    @property
    def bakiye(self):
        return self.__bakiye

    def yatir(self, miktar):
        if miktar > 0:
            self.__bakiye += miktar

    def cek(self, miktar):
        if 0 < miktar <= self.__bakiye:
            self.__bakiye -= miktar
            return True
        return False


class ATM:
    def __init__(self):
        self.hesap = None
    
    def giris(self, hesap, sifre):
        if hesap.sifre == sifre:
            self.hesap = hesap
            return True
        return False
    
    def yatir(self, para):
        self.hesap.yatir(para)
    
    def cek(self, para):
        return self.hesap.cek(para)

hesap = Hesap("1234", 1000)
atm = ATM()

if atm.giris(hesap, "1234"):
    print(f"Bakiye: {atm.hesap.bakiye}")
    atm.yatir(500)
    print(f"Bakiye: {atm.hesap.bakiye}")
    atm.cek(200)
    print(f"Bakiye: {atm.hesap.bakiye}")
    