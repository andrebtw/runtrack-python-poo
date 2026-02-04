class Livre:
    def __init__(self, titre:str, auteur:str, page_count:int):
        if not isinstance(titre, str):
            raise ValueError
        if not isinstance(auteur, str):
            raise ValueError
        if not isinstance(page_count, int):
            raise ValueError
    
        self.__titre = titre
        self.__auteur = auteur
        self.__page_count = page_count
        self.__disponible = True
    
    def verification(self):
        return self.__disponible

    def set_titre(self, titre):
        self.__titre = titre
    
    def set_auteur(self, auteur):
        self.__auteur = auteur
    
    def set_page_count(self, page_count:int):
        if not isinstance(page_count, int):
            return
        if page_count < 0:
            return

        self.__page_count = page_count
    
    def emprunter(self):
        if self.verification():
            self.__disponible = False

    def rendre(self):
        if not self.verification():
            self.__disponible = True

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur
    
    def get_page_count(self):
        return self.__page_count

l=Livre("test", "e", 4)
l.set_page_count(-1)
print(l.get_page_count())
l.emprunter()
print(l.verification())
l.rendre()
print(l.verification())