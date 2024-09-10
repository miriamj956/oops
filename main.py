class Pets: 
    def __init__(self, animal, color, name):
        self.animal = animal
        self.color = color
        self.name = name
    
    def show(self):
        print("The pet details are: ")
        print("Type of animal: ", self.animal)
        print("Pet color: ", self.color)
        print("Pet name: ", self.name)

p1 = Pets("tiger", "orange", "bruce" )
p1.show()