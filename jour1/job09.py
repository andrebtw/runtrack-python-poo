class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prixHT = prix
        self.TVA = 20
    
    def CalculerPrixTTC(self):
        return self.prixHT * (1 + (self.TVA/100))

    def afficher(self):
        print(f"Nom: {self.nom}; prixHT: {self.prixHT}; TVA: {self.TVA}")
    
    def set_nom(self, nom):
        self.nom = nom
    
    def set_prix(self, prix):
        self.prix = prix
    
    def get_nom(self):
        return self.nom

    def get_prix(self):
        return self.prixHT
    
    def get_TVA(self):
        return self.TVA

p=Produit("test", 1)
print(p.CalculerPrixTTC())
p.afficher()