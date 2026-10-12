def addition(a, b):
    return a + b


def soustraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def choix_menu():
    print("-------")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")


choix_valide = ["1", "2", "3", "4"]

choix_menu()
choix_utilisateur = input("Votre choix de calcul : ")

while choix_utilisateur not in choix_valide:
    choix_utilisateur = input("Votre choix de calcul : ")

a = float(input("Premier nombre : "))
b = float(input("Deuxième nombre : "))

if choix_utilisateur == "1":
    print(addition(a, b))
elif choix_utilisateur == "2":
    print(soustraction(a, b))
elif choix_utilisateur == "3":
    print(multiplication(a, b))
elif choix_utilisateur == "4":
    if b == 0:
        print("Erreur : division par zéro")
    else:
        print(division(a, b))
