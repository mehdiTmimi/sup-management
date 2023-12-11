from Animal import Animal
class Tigre(Animal):
    def __init__(self,race,poids):
        #super().__init__(race,poids)
        Animal.__init__(self,race,poids)
    def __str__(self):
        #return f"Tigre : {super().__str__()}"
        return f"Tigre : {Animal.__str__(self)}"
    def crier(self):
        print("Tigre : GRRRRRRRRR")
