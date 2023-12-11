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
    print(" 4 - quitter")
    return int(input("entrer votre choix ( 1 à 4)"))
def infoZoo():
    print(f"le {zoo['nom']} se trouve à {zoo['address']}")
    for animal in zoo["animaux"]:
        print(animal)
def ajouterAnimal():
    type = input("veuillez choisir le type (Elephant:0,Tigre:1)")
    race = input("donner la race")
    poids = input("donner le poids")
    if type == "0":
        zoo["animaux"].append(Elephant(race,poids))
    else:
        zoo["animaux"].append(Tigre(race,poids))
def crieAnimaux():
    for animal in zoo["animaux"]:
        animal.crier()
choix = 0
while choix!=4:
    choix = menu()
    if choix==1:
        infoZoo()
    elif choix == 2 :
        ajouterAnimal()
    elif choix == 3 :
        crieAnimaux()
    elif choix == 4 :
        print("Au revoir")
    else:
        print("choix incorrecte")

