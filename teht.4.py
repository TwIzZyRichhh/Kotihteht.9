import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdytä(self, muutos):
        uusi_nopeus = self.nopeus + muutos
        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus

    def kulje(self, tunnit):
        matkattu = self.nopeus * tunnit
        self.kuljettu_matka += matkattu

    def tulosta_ominaisuudet(self):
        return (self.rekisteritunnus, self.huippunopeus, self.nopeus, round(self.kuljettu_matka, 2))

autot = []
for i in range(1, 11):  # 10 autoa
    rekisteritunnus = f"ABC-{i}"
    huippunopeus = random.randint(100, 200)
    autot.append(Auto(rekisteritunnus, huippunopeus))

kilpailu_kaynnissa = True
while kilpailu_kaynnissa:
    for auto in autot:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdytä(nopeuden_muutos)

        auto.kulje(1)

        if auto.kuljettu_matka >= 10000:
            kilpailu_kaynnissa = False
            break

print(
    f"{'Rekisteritunnus':<15}{'Huippunopeus (km/h)':<20}{'Tämänhetkinen nopeus (km/h)':<30}{'Kuljettu matka (km)':<20}")
print("=" * 85)
for auto in autot:
    rekisteritunnus, huippunopeus, nopeus, kuljettu_matka = auto.tulosta_ominaisuudet()
    print(f"{rekisteritunnus:<15}{huippunopeus:<20}{nopeus:<30}{kuljettu_matka:<20}")
