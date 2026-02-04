class InvalidCommandStatusError(Exception):
    pass

class Commande:
    def __init__(self, commande_nb, liste_plats, status_commande):
        self.__commande_nb = commande_nb
        self.__liste_plats = liste_plats
        if status_commande in ["en cours", "terminée", "annulée"]:
            self.__status_commande = status_commande
        else:
            raise InvalidCommandStatusError(
                "Invalid status name"
            )
    
    def ajouter_plat(self, plat:str):
        self.__liste_plats.append(plat)
    
    def annuler_commande(self):
        self.__status_commande = "annulée"
    
    def __calculer_total(self):
        total = 0
        if self.__status_commande == "terminée":
            for plat, prix in self.__liste_plats.items():
                total += prix
        
        return total
    
    def __calculer_total_TVA(self):
        return self.__calculer_total() * 1.2
    
    def afficher_total(self):
        print(f"Total à payer: {self.__calculer_total()}")
        print(f"Numéro de commande: {self.__commande_nb}")
        print(f"Total à payer + TVA: {self.__calculer_total_TVA()}")
        

c=Commande(2, {"pad thai":15, "bolognaise":13, "mousse au chocolat":3, "tarte au citron":3}, "terminée")
c.afficher_total()