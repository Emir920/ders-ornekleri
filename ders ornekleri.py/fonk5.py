import random
import argparse


class Dusman:
    def __init__(self, ad, can, guc):
        self.ad = ad
        self.can = can
        self.guc = guc

    def saldir(self, hedef):
        hedef.can -= self.guc
        return f"{self.ad} {hedef.ad}'a {self.guc} hasar verdi. Kalan can: {hedef.can}"


class DusmanUyarisi(Dusman):
    def __init__(self, ad, can, guc, uyari_seviyesi):
        super().__init__(ad, can, guc)
        self.uyari_seviyesi = uyari_seviyesi


class Oyuncu:
    def __init__(self, ad, can, guc, iksir=3):
        self.ad = ad
        self.can = can
        self.max_can = can
        self.guc = guc
        self.iksir = iksir

    def saldir(self, hedef):
        hedef.can -= self.guc
        return f"{self.ad} {hedef.ad}'a {self.guc} hasar verdi. Hedef can: {hedef.can}"

    def iyilestir(self):
        if self.iksir <= 0:
            return "İksirin yok!"
        iyile = min(30, self.max_can - self.can)
        if iyile <= 0:
            return "Zaten tam canlisin."
        self.can += iyile
        self.iksir -= 1
        return f"{self.ad} {iyile} can iyileşti. Kalan can: {self.can}. Kalan iksir: {self.iksir}"


def yeni_dusmanlar():
    return [
        Dusman("Ork", 100, 15),
        Dusman("Goblin", 80, 10),
        Dusman("Troll", 150, 20),
        DusmanUyarisi("Ejderha", 300, 50, "Yuksek"),
    ]


def oyun(derslik_oyuncu=None):
    oyuncu = derslik_oyuncu or Oyuncu("Kahraman", 200, 25, iksir=3)
    dusmanlar = yeni_dusmanlar()

    print("--- Baslangic: Kucuk Terminal RPG ---")
    while oyuncu.can > 0 and any(d.can > 0 for d in dusmanlar):
        print(f"\nOyuncu: {oyuncu.ad} Can: {oyuncu.can} Iksir: {oyuncu.iksir}")
        print("Dusmanlar:")
        for i, d in enumerate(dusmanlar, 1):
            status = f"{d.can} can" if d.can > 0 else "(oldu)"
            print(f" {i}. {d.ad} - {status}")

        print("\nSecenekler: 1) Saldir  2) Iyilestir  3) Kac")
        sec = input("Seciminiz: ").strip()
        if sec == "1":
            idx = input("Hangi dusmana? (sayi): ").strip()
            if not idx.isdigit() or int(idx) < 1 or int(idx) > len(dusmanlar):
                print("Gecersiz secim.")
                continue
            hedef = dusmanlar[int(idx) - 1]
            if hedef.can <= 0:
                print("Bu dusman zaten olmus.")
                continue
            print(oyuncu.saldir(hedef))
            if hedef.can <= 0:
                print(f"{hedef.ad} yendi!")
        elif sec == "2":
            print(oyuncu.iyilestir())
        elif sec == "3":
            print("Kacmaya calisiyorsunuz...")
            if random.random() < 0.5:
                print("Kactin! Oyun sonlandi.")
                return
            else:
                print("Kacma basarisiz.")
        else:
            print("Gecersiz secenek.")
            continue

        # Dusmanlar saldirir
        for d in dusmanlar:
            if d.can > 0:
                print(d.saldir(oyuncu))
                if oyuncu.can <= 0:
                    print("Oyuncu yendi. Oyun bitti.")
                    return

    if oyuncu.can > 0:
        print("Tebrikler! Tum dusmanlari yendiniz.")
    else:
        print("Malesef kaybettiniz.")


def auto_run():
    # Hicbir girdi gerekmeden otomatik kosullar altinda bir tur calistir
    oyuncu = Oyuncu("Bot", 200, 25, iksir=3)
    dusmanlar = yeni_dusmanlar()
    rnd = random.Random(0)
    steps = 0
    while oyuncu.can > 0 and any(d.can > 0 for d in dusmanlar) and steps < 200:
        # basit strateji: en dusuk canli dusmana saldir
        hedefler = [d for d in dusmanlar if d.can > 0]
        hedef = min(hedefler, key=lambda x: x.can)
        oyuncu.saldir(hedef)
        for d in dusmanlar:
            if d.can > 0:
                d.saldir(oyuncu)
        if oyuncu.can < 50 and oyuncu.iksir > 0:
            oyuncu.iyilestir()
        steps += 1
    if oyuncu.can > 0:
        print("AUTO RUN: Bot kazandi")
    else:
        print("AUTO RUN: Bot kaybetti")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--auto", action="store_true", help="Otomatik test calistir")
    args = parser.parse_args()
    if args.auto:
        auto_run()
    else:
        oyun()