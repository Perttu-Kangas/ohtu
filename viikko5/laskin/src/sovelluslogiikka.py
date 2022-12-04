class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen = None

    def miinus(self, arvo):
        self.aseta_arvo(self.tulos - arvo)

    def plus(self, arvo):
        self.aseta_arvo(self.tulos + arvo)

    def nollaa(self):
        self.aseta_arvo(0)

    def aseta_arvo(self, arvo):
        self.edellinen = self.tulos
        self.tulos = arvo
    
    def kumoa(self):
        if self.edellinen:
            self.tulos = self.edellinen
        self.edellinen = None

class Summa:
    def __init__(self, sovellus, syote):
        self.sovellus = sovellus
        self.syote = syote

    def suorita(self):
        return self.sovellus.plus(int(self.syote()))

class Erotus:
    def __init__(self, sovellus, syote):
        self.sovellus = sovellus
        self.syote = syote

    def suorita(self):
        return self.sovellus.miinus(int(self.syote()))

class Nollaus:
    def __init__(self, sovellus, syote):
        self.sovellus = sovellus
        self.syote = syote

    def suorita(self):
        return self.sovellus.nollaa()

class Kumoa:
    def __init__(self, sovellus, syote):
        self.sovellus = sovellus
        self.syote = syote

    def suorita(self):
        return self.sovellus.kumoa()
