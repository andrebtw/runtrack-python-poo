class Ville:
    def __init__(self, nom:str, habitants:int):
        self.__nom = nom
        self.__habitants = habitants
    
    def add_habitants(self, count):
        self.__habitants += count
    
    def get_habitants(self):
        return self.__habitants
    
    def get_nom(self):
        return self.__nom
    

class Personne:
    def __init__(self, nom:str, age:int, ville:Ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.__ajouterPopulation(self.__ville)
    
    @staticmethod
    def __ajouterPopulation(ville):
        ville.add_habitants(1)

paris = Ville("Paris", 10000000)
marseille = Ville("Marseille", 861635)

# print(marseille.get_habitants())

print(f"Population de la ville de {paris.get_nom()}: {paris.get_habitants()} habitants")
print(f"Population de la ville de {marseille.get_nom()}: {marseille.get_habitants()} habitants")

john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

print(f"Population de la ville de {paris.get_nom()}: {paris.get_habitants()} habitants")
print(f"Population de la ville de {marseille.get_nom()}: {marseille.get_habitants()} habitants")