class Tache:
    def __init__(self, titre, desc, status):
        self.__titre = titre
        self.__desc = desc
        self.__status = status

    def get_title(self):
        return self.__titre
    
    def get_desc(self):
        return self.__desc
    
    def get_status(self):
        return self.__status
    
    def set_status(self, status:str):
        self.__status = status
        

class ListeDeTaches:
    def __init__(self):
        self.__taches = []

    def ajouterTache(self, tache:Tache):
        self.__taches.append(tache)
    
    def supprimerTache(self, tache:Tache):
        self.__taches.remove(tache)

    def marquerCommeFinie(self, tache):
        tache.set_status("terminer")
    
    def afficherListe(self):
        for tache in self.__taches:
            
    
    def filterListe(self, status):
        list = []

        for tache in self.__taches:
            if tache.get_status() == status:
                list.append(tache)
        
        return list


une_tache = Tache("Test1", "desc", "à faire")
tache2 = Tache("Test2", "desc", "à faire")
tache3= Tache("Test3", "desc", "à faire")

liste = ListeDeTaches()

liste.ajouterTache(une_tache)
liste.ajouterTache(tache2)
liste.ajouterTache(tache3)

print(liste.afficherListe())