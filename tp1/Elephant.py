from Animal import Animal
class Elephant(Animal):
    def __init__(self,race,poids):
        #super().__init__(race,poids)
        Animal.__init__(self,race,poids)
    def __str__(self):
        #return f"Elephant : {super().__str__()}"
        return f"Elephant : {Animal.__str__(self)}"
    def crier(self):
        print("Elephant : uHoUuUuUu")
