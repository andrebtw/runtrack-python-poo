class Voiture:
    def __init__(self, marque:str, modele:str, annee:int, km:int):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__km = km
        self.__en_marche = False
        self.__reservoir = 50
    
    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
    
    def arreter(self):
        self.__en_marche = False

    def set_marque(self, marque:str):
        self.__marque = marque
    
    def set_modele(self, modele:str):
        self.__modele = modele
    
    def set_annee(self, annee:int):
        self.__annee = annee
    
    def set_km(self, km:int):
        self.__km = km
    
    def __verifier_plein(self):
        return self.__reservoir

    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele
    
    def get_annee(self):
        return self.__annee
    
    def get_km(self):
        return self.__km

v = Voiture("Mercedes", "C 220", 2004, 400000)
v.demarrer()
print(v.get_modele())
print(v.get_annee())