class Part:
    def __init__(self, name, material):
        self.name = name 
        self.material = material

    def change_material(self, new_material):
        self.material = new_material
        return self.material
    
    def __str__(self):
        description = f"notre nom c'est {self.name} et notre material est {self.material}"
        return description

    def print_part_ptr(self):
        print(hex(id(self)))


class Ship:
    def __init__(self, nom:str, parts):
        self.nom = nom
        self.__parts = parts
    
    def display_state(self):
        for obj in self.__parts.values():
            print(obj.__str__())

    ##Implémentez une méthode replace_part(part_name,
    ##new_part) pour remplacer une pièce existante.
    
    def replace_part(self, part_name, new_part):
        try:
            self.__parts[part_name].name = new_part
            self.__parts[new_part] = self.__parts.pop(part_name)
        except:
            print("Wrong part name!")
            exit(1)
    
    def change_part(self, part_name, new_material):
        try:
            self.__parts[part_name].change_material(new_material)
        except:
            print("Wrong part name!")
            exit(1)

    def print_part_ptr(self, part):
        print(hex(id(self.__parts[part.name])))

class RacingShip:
    def __init__(self):
        pass

part1 = Part("devant", "Bois")
part2 = Part("deriere", "Fer")
part3 = Part("bas", "plastique")
part4 = Part("DdD", "Metal")
part5 = Part("DxD", "Bois")

dict = {
    part1.name: part1,
    part2.name: part2,
    part3.name: part3,
    part4.name: part4,
    part5.name: part5,
}

s=Ship("Navire", dict)

s.change_part("devant", "TestBois")
s.replace_part("DdD", part2)

s.display_state()

part1.print_part_ptr()
s.print_part_ptr(part1)