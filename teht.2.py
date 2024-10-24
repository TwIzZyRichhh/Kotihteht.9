class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def tulosta_ominaisuudet(self):
        print(f"Rekisteritunnus: {self.rekisteritunnus}")
        print(f"Huippunopeus: {self.huippunopeus} km/h")
        print(f"Tämänhetkinen nopeus: {self.nopeus} km/h")
        print(f"Kuljettu matka: {self.kuljettu_matka} km")

    def kiihdytä(self, muutos):
        uusi_nopeus = self.nopeus + muutos
        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus
        print(f"Uusi nopeus on {self.nopeus} km/h")


auto = Auto("ABC-123", 142)

auto.tulosta_ominaisuudet()
auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
print(f"Tämänhetkinen nopeus: {auto.nopeus} km/h")
auto.kiihdytä(-200)
print(f"Tämänhetkinen nopeus: {auto.nopeus} km/h")
