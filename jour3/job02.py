class CompteBancaire:
    def __init__(self, id:int, nom:str, prenom:str, solde:int, droit_decouvert):
        self.__id = id
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert_on = droit_decouvert
    
    def get_id(self):
        return self.__id
    
    def get_prenom(self):
        return self.__prenom
    
    def get_nom(self):
        return self.__nom

    def afficher(self):
        print(f"Numéro de compte: {self.__id}")
        print(f"Nom: {self.__nom}")
        print(f"Prénom: {self.__prenom}")

    def afficherSolde(self):
        print(f"Solde: {self.__solde}")

    def versement(self, income):
        self.__solde += income
    
    def virement(self, compte:CompteBancaire, montant):
        if compte.get_id() == self.get_id():
            print("Un virement ne peu pas etre effectuer vers le meme compte.")
            return
        elif self.__solde - montant < 0 and self.__decouvert_on is False:
            print("Pas assez de solde sur le compte.")
            return

        self.__solde -= montant
        compte.versement(montant)
        print(f"Le virement a bien été effectuer depuis le compte de {self.get_prenom()} {self.get_nom()} vers le compte de {compte.get_prenom()} {compte.get_nom()}")
    
    def retrait(self, withdraw:int):
        if not isinstance(withdraw, int):
            print("Un entier svp.")
            return
        elif self.__solde - withdraw < 0 and self.__decouvert_on is False:
            print("Pas assez de solde sur le compte.")
            return

        self.__solde -= withdraw

    def agios(self, agios):
        self.__solde = self.__solde * (1 + (agios/100))
    
test1 = CompteBancaire(420, "Louis", "Jean", 0, False)
test2 = CompteBancaire(421, "Filip", "Max", 0, False)
# test1.versement(1000)
# test1.retrait(12.1)
# test1.retrait(1751)
test1.retrait(2000)
test1.agios(20)
test1.afficher()
test1.afficherSolde()
test1.virement(test2, 100)
test2.afficher()
test2.afficherSolde()