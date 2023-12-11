class Animal:
    def __init__(this,race,poids):
        this.race = race
        this.poids = poids
    def __str__(self): #toString En Java
        #return "- race : " + str(self.race) + " , poids :" + str(self.poids) + " kg."
        return f"-race : {self.race}, poids : {self.poids} kg."
    def crier(self):
        pass
