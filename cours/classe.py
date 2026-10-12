def ajouter(nom, liste):
    if nom in liste:
        print("Le nom est déjà dedans")
    return liste.append(nom)

def supprimer(nom, liste):
    if nom not in liste:
        print("Nom non trouvé")
    while True:
        confirmation = input("Voulez-vous vraiment supprimer ce nom ? (o/n) : ")
        if confirmation == "o":
            return liste.remove(nom)
        elif confirmation == "n":
            print("Nom non supprimé")
        else:
            print("Choix invalide")

def rechercher(nom, liste):
    resultats = [nom for nom in liste if nom in nom]
    if not resultats:
        print("Nom non trouvé")
    else:
        print("Nom trouvé")
    return resultats

def afficher(liste):
    return liste

def modifier(nom, nouveau_nom, liste):
    if nom not in liste:
        print("Nom non trouvé")
    index = liste.index(nom)
    liste[index] = nouveau_nom
    return liste

def nombre_de_noms(liste):
    return len(liste)

def rechercher(nom, liste):
    if nom not in liste:
        print("Nom non trouvé")
    print("Nom trouvé")

def choix_menu():
    print("1. Ajouter un nom")
    print("2. Supprimer un nom")
    print("3. Afficher la liste des noms")
    print("4. Modifier un nom")
    print("5. Nombre de noms")
    print("6. Rechercher un nom")
    print("7. Quitter")
    return input("Votre choix : ")


liste = []
while True:
    choix = choix_menu()
    if choix == "1":
        nom = input("Entrez le nom à ajouter : ")
        ajouter(nom, liste)
    elif choix == "2":
        nom = input("Entrez le nom à supprimer : ")
        supprimer(nom, liste)
    elif choix == "3":
        print(afficher(liste))
    elif choix == "4":
        nom = input("Entrez le nom à modifier : ")
        nouveau_nom = input("Entrez le nouveau nom : ")
        modifier(nom, nouveau_nom, liste)
    elif choix == "5":
        print(nombre_de_noms(liste))
    elif choix == "6":
        nom = input("Entrez le nom à rechercher : ")
        rechercher(nom, liste)
    elif choix == "quit":
        break
    else:
        print("Choix invalide")
