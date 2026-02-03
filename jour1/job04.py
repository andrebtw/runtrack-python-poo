class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def SePresenter(self):
        return f"{self.nom}, {self.prenom}"

p = Personne("john", "doe")
print(p.SePresenter())
