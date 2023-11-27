class Calculatrice:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return "a = " + str(self.a) + " et b = " + str(self.b)
    def somme(self):
        return self.a+self.b

calculatrice = Calculatrice(5,9)
print(calculatrice)
print(calculatrice.somme())