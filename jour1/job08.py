import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
        self.changerRayon(self.rayon)
    
    def changerRayon(self, r):
        self.rayon = r
        self.diametre = self.rayon * 2
        self.circonference = math.pi * self.diametre
        self.air = math.pi * (self.rayon ** 2)
    
    def afficherInfos(self):
        print(f"Rayon: {self.rayon}; Diametre: {self.diametre}; Circonference: {self.circonference}; aire: {self.air}")

c=Cercle(5)
c.afficherInfos()