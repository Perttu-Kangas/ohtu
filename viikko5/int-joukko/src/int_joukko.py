KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = KAPASITEETTI if kapasiteetti is None else kapasiteetti
        self.kasvatuskoko = OLETUSKASVATUS if kasvatuskoko is None else kasvatuskoko

        self.joukko = []

    def kuuluu(self, n):
        return n in self.joukko

    def lisaa(self, n):
        if self.kuuluu(n):
            return False

        if self.kapasiteetti - 1 < self.mahtavuus():
            self.joukko.append(n)
            return True
        
        self.kapasiteetti += self.kasvatuskoko
        self.joukko.append(n)
        return True

    def poista(self, n):
        if self.kuuluu(n):
            self.joukko.remove(n)

    def mahtavuus(self):
        return len(self.joukko)

    def to_int_list(self):
        return self.joukko

    @staticmethod
    def yhdiste(a, b):
        joukko = IntJoukko()
        for i in a.to_int_list():
            joukko.lisaa(i)
        for i in b.to_int_list():
            if not joukko.kuuluu(i):
                joukko.lisaa(i)
        return joukko

    @staticmethod
    def leikkaus(a, b):
        joukko = IntJoukko()
        for i in a.to_int_list():
            if b.kuuluu(i):
                joukko.lisaa(i)
        return joukko
    
    @staticmethod
    def erotus(a, b):
        joukko = IntJoukko()
        for i in a.to_int_list():
            if not b.kuuluu(i):
                joukko.lisaa(i)
        return joukko

    def __str__(self):
        return "{%s}" % (", ".join(str(i) for i in self.to_int_list()),)
