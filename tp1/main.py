from Elephant import Elephant
from Tigre import Tigre


zoo = {
    "nom" : "fes zoo",
    "address":"centre ville 19 fes maroc",
    "animaux":list() #[]
}

def menu():
    print("-----------------Menu-----------------")
    print(" 1 - Infos du Zoo")
    print(" 2 - Ajouter un animal au Zoo")
    print(" 3 - les cries des animaux")
    print(" 4 - supprimer un animal")
    print(" 5 - quitter")
    return int(input("entrer votre choix ( 1 à 4)"))
def infoZoo():
    print(f"le {zoo['nom']} se trouve à {zoo['address']}")
    for animal in zoo["animaux"]:
        print(animal)
def ajouterAnimal():
    type = input("veuillez choisir le type (Elephant:0,Tigre:1)")
    race = input("donner la race")
    poids = input("donner le poids")
    try:
        if poids.isnumeric()==False:
            raise Exception("the weight must be a numeric value")
        if type == "0":
            zoo["animaux"].append(Elephant(race,poids))
        else:
            zoo["animaux"].append(Tigre(race,poids))
    except Exception as e:
        print(str(e))
    
def crieAnimaux():
    for animal in zoo["animaux"]:
        animal.crier()
def deleteAnimal():
    """
    indice  = 0
    for animal in zoo["animaux"]:
        print(f"{indice} : {animal}")
        indice = indice + 1 
    """
    for i, animal in enumerate(zoo["animaux"]):
        # https://www.geeksforgeeks.org/iterate-over-a-list-in-python/
        print(f"{i} : {animal}")
    pos = int(input("donnez la position de l'animal : "))
    zoo["animaux"].pop(pos)
    print("animal est supprimé")
    
choix = 0
zoo["animaux"].append(Elephant("africain",1000))
zoo["animaux"].append(Tigre("africain",200))
while choix!=5:
    choix = menu()
    if choix==1:
        infoZoo()
    elif choix == 2 :
        ajouterAnimal()
    elif choix == 3 :
        crieAnimaux()
    elif choix == 4 :
        deleteAnimal()
    elif choix == 5 :
        print("Au revoir")
    else:
        print("choix incorrecte")

