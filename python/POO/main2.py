class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Etudiant(Person):
  def __init__(self,fname,lname,cne):
    Person.__init__(self, fname, lname)
    self.cne= cne
  def printname(self):
    Person.printname(self)
    print(self.cne)
p = Etudiant("mehdi","tmimi","cd22342")
p.printname()
