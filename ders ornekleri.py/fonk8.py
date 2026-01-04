class Hesap:
    def __init__(self, sifre, bakiye=0):
        self.sifre = sifre
        self.bakiye = bakiye


class ATM:
    def __init__(self):
        self.hesap = None
    
    def giris(self, hesap, sifre):
        if hesap.sifre == sifre:
            self.hesap = hesap
            return True
        return False
    
    def yatir(self, para):
        self.hesap.bakiye += para
    
    def cek(self, para):
        self.hesap.bakiye -= para

hesap = Hesap("1234", 1000)
atm = ATM()

if atm.giris(hesap, "1234"):
    print(f"Bakiye: {atm.hesap.bakiye}")
    atm.yatir(500)
    print(f"Bakiye: {atm.hesap.bakiye}")
    atm.cek(200)
    print(f"Bakiye: {atm.hesap.bakiye}")

