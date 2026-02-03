class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1
    
    def nommer(self, str:str):
        self.prenom = str

a = Animal()
a.vieillir()
a.nommer("test")
print(a.prenom)