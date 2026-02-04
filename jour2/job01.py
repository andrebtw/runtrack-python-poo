class Rectangle:
    def __init__(self, l, largeur):
        self.__longueur = l
        self.__largeur = largeur
    
    def set_longeur(self, v):
        self.__longueur = v
    
    def set_largeur(self, v):
        self.__largeur = v
    
    def get_longeur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur

r=Rectangle(4, 5)
r.set_largeur(420)
print(r.get_largeur())