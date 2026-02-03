class Point:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
    
    def afficherLesPoints(self):
        print(self.x, self.y)
    
    def afficherX(self):
        print(self.x)
    
    def afficherY(self):
        print(self.y)
    
    def changerX(self, x):
        self.x = x
    
    def changerY(self, y):
        self.y = y

p = Point(5, 3)
p.afficherLesPoints()
p.changerX(0)
p.afficherX()