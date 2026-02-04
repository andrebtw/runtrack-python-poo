class Student:
    def __init__(self, nom, prenom, id):
        self.__nom = nom
        self.__prenom = prenom
        self.__id = id
        self.__credits = 0
        self.__level = self.__studentEval()
    
    def add_credits(self, incoming_credits:int):
        if incoming_credits > 0:
            self.__credits += incoming_credits
    
    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
    
    def studentInfo(self):
        print(f"Nom = {self.__nom}\nPrénom = {self.__prenom}\nid = {self.__id}\nNiveau = {self.__studentEval()}")
    

john=Student("Doe", "John", 145)
john.add_credits(30)
john.add_credits(30)
john.add_credits(29)
john.studentInfo()