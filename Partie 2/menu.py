import random
import crew

john = crew.Operator("John", "Doe", "M", 30, "technicien")
john.experience = 5
jane = crew.Operator("Jane", "Doe", "F", 25, "pilote")
jane.experience = 10

ship = crew.Spaceship("Enterprise", "guerre", "opérationnel")
ship.add_member(john)
ship.add_member(jane)

fleet = crew.Fleet("Fondation")
fleet.add_spaceship(ship)


def add_member(ship):

    new_first_name = input("Prénom du membre d'équipage : ")
    new_last_name = input("Nom du membre d'équipage : ")
    new_gender = input("Sexe du membre d'équipage : ")
    new_age = int(input("Âge du membre d'équipage : "))
    new_role = input("Rôle du membre d'équipage : ")

    if len(new_first_name) < 3 or len(new_first_name) > 15 or len(new_last_name) < 3 or len(new_last_name) > 15:
        print("Le nom et le prénom doivent contenir entre 3 et 15 caractères")
        return ship

    if new_age < 18 and new_role == "pilote":
        print("Pour être pilot il faut avoir au moins 18 ans")
        return ship
    if new_age < 25 and new_role == "technicien":
        print("Pour être technicien il faut avoir au moins 25 ans")
        return ship
    if new_age > 65:
        print("Pour être dans l'équipage il faut avoir moins de 65 ans")
        return ship

    experience = 0
    if new_role == "technicien":
        experience = int(input("Expérience du membre d'équipage : "))
        if experience < 0:
            print("Pas possible d'avoir une expérience négative...")
            return ship

    for member in ship.crew:
        if member.first_name == new_first_name and member.last_name == new_last_name:
            print("Ce membre est déjà dans l'équipage")
            return ship

    if new_role == "mentaliste":
        new_member = crew.Mentalist(new_first_name, new_last_name, new_gender, new_age)
    else:
        new_member = crew.Operator(new_first_name, new_last_name, new_gender, new_age, new_role)
        new_member.experience = experience

    ship.add_member(new_member)
    return ship


def remove_member(ship):

    remove_last_name = input("Nom du membre à retirer : ")
    for member in ship.crew:
        if member.last_name == remove_last_name:
            ship.crew.remove(member)
            return ship
    print("Ce membre n'est pas dans l'équipage")
    return ship


def display_crew(ship):

    if ship.crew == []:
        print("Aucun membre dans l'équipage")
    for member in ship.crew:
        if type(member) == crew.Operator:
            print(f"Nom : {member.last_name} - Prénom : {member.first_name} - Sexe : {member.gender} - Âge : {member.age} - Rôle : {member.role} - Expérience : {member.experience} ans")
        else:
            print(f"Nom : {member.last_name} - Prénom : {member.first_name} - Sexe : {member.gender} - Âge : {member.age} - Rôle : mentaliste - Mana : {member.mana}")
    return ship


def check_crew(ship):

    if len(ship.crew) < 2:
        print("L'équipage doit contenir au moins 2 membres")
        return ship

    if ship.check_preparation() == True:
        print("L'équipage est prêt pour la mission !")
    else:
        print("L'équipage n'est pas prêt")
    return ship


def random_events(ship):

    if ship.crew == []:
        print("Aucun membre dans l'équipage")
        return ship

    events = random.choice(["promu", "démission"])
    if events == "démission":
        member = random.choice(ship.crew)
        ship.crew.remove(member)
        print(f"Le membre {member.first_name} {member.last_name} a démissionné")
    else:
        print("Un membre de l'équipage a été promu")
    return ship


def promote_member(ship):

    last_name = input("Nom du membre à promouvoir : ")
    first_name = input("Prénom du membre à promouvoir : ")
    for member in ship.crew:
        if member.last_name != last_name or member.first_name != first_name:
            continue
        if type(member) != crew.Operator or member.role != "technicien":
            print("Ce membre n'est pas un technicien")
            return ship
        if member.experience < 10:
            print("Ce membre d'équipage n'a pas assez d'expérience pour être promu")
            return ship
        if member.age < 18 or member.age > 65:
            print("Ce membre d'équipage n'a pas l'âge requis pour être promu")
            return ship
        member.role = "pilote"
        print(f"Le membre {member.first_name} {member.last_name} a été promu pilote bien joué à lui")
        return ship
    print("Ce membre n'est pas dans l'équipage")
    return ship


def crew_report(fleet):

    total = 0
    for ship in fleet.spaceships:
        total = total + len(ship.crew)

    if total == 0:
        print("Aucun membre dans l'équipage")
        return fleet

    fleet.statistics()

    for ship in fleet.spaceships:
        for member in ship.crew:
            if member.age >= 60:
                print(f"Le membre {member.first_name} {member.last_name} est bientôt à la retraite")
    return fleet


def menu(ship, fleet):

    counter_events = 0
    while True:
        print(" [1] Ajouter un membre d'équipage")
        print(" [2] Retirer un membre d'équipage")
        print(" [3] Afficher l'équipage")
        print(" [4] Vérifier si l'équipage est prêt")
        print(" [5] Promouvoir un technicien")
        print(" [6] Afficher le rapport de l'équipage")
        print(" [7] Quitter")

        choice = input("Choisissez une option  : ")
        match choice:
            case "1":
                add_member(ship)
                counter_events += 1
            case "2":
                remove_member(ship)
                counter_events += 1
            case "3":
                display_crew(ship)
                counter_events += 1
            case "4":
                check_crew(ship)
                counter_events += 1
            case "5":
                promote_member(ship)
                counter_events += 1
            case "6":
                crew_report(fleet)
                counter_events += 1
            case "7":
                break
            case _:
                print("Option invalide")
        if counter_events == 5:
            random_events(ship)
            counter_events = 0


menu(ship, fleet)
