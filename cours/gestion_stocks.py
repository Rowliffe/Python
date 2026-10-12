def ajouter_stock(stock, produit, quantite):
    if produit in stock:
        stock[produit] += quantite
    else:
        stock[produit] = quantite
    return stock
 

def supprimer_stock(stock, produit):
    if produit not in stock:
        print("Produit non trouvé")
    else:
        del stock[produit]
        print("Produit supprimé")
    return stock


def afficher_stock(stock):
    if not stock:
        print("Stock vide")
        return stock
    for produit in sorted(stock.keys()):
        print(f"{produit} : {stock[produit]}")
    return stock


def rechercher_stock(stock, produit):
    if produit not in stock:
        print("Produit non trouvé")
    else:
        print(f"Produit trouvé — {produit} : {stock[produit]}")
    return stock


def modifier_nom_produit(stock, ancien_nom, nouveau_nom):
    if ancien_nom not in stock:
        print("Produit non trouvé")
    elif nouveau_nom in stock:
        print("Un produit avec ce nom existe déjà")
    else:
        stock[nouveau_nom] = stock.pop(ancien_nom)
        print("Produit modifié")
    return stock


def modifier_quantite(stock, produit, quantite):
    if produit not in stock:
        print("Produit non trouvé")
    else:
        stock[produit] = quantite
        print("Quantité modifiée")
    return stock


def quantite_totale(stock):
    return sum(stock.values())


def choix_menu():
    print("1. Ajouter un produit")
    print("2. Supprimer un produit")
    print("3. Afficher le stock (ordre alphabétique)")
    print("4. Rechercher un produit")
    print("5. Quantité totale en stock")
    print("6. Modifier un produit (nom)")
    print("7. Modifier la quantité d'un produit")
    print("8. Quitter")
    return input("Votre choix : ")


stock = {}
while True:
    choix = choix_menu()
    if choix == "1":
        produit = input("Nom du produit : ")
        quantite = int(input("Quantité : "))
        ajouter_stock(stock, produit, quantite)
    elif choix == "2":
        produit = input("Nom du produit à supprimer : ")
        supprimer_stock(stock, produit)
    elif choix == "3":
        afficher_stock(stock)
    elif choix == "4":
        produit = input("Nom du produit à rechercher : ")
        rechercher_stock(stock, produit)
    elif choix == "5":
        print(f"Quantité totale : {quantite_totale(stock)}")
    elif choix == "6":
        ancien = input("Nom actuel du produit : ")
        nouveau = input("Nouveau nom : ")
        modifier_nom_produit(stock, ancien, nouveau)
    elif choix == "7":
        produit = input("Nom du produit : ")
        quantite = int(input("Nouvelle quantité : "))
        modifier_quantite(stock, produit, quantite)
    elif choix == "8":
        print("Au revoir")
        break
    else:
        print("Choix invalide")
