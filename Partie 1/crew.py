import random 


crew = [
    {
        "first_name": "John",
        "last_name": "Doe",
        "gender": "M",
        "age": 30,
        "role": "technicien",
        "experience": 5,
    },
    {
        "first_name": "Jane",
        "last_name": "Doe",
        "gender": "F",
        "age": 25,
        "role": "pilote",
        "experience": 10,
    },
]


def add_member(crew):
    new_first_name = input("Prénom du membre d'équipage : ")
    new_last_name = input("Nom du membre d'équipage : ")
    new_gender = input("Sexe du membre d'équipage : ")
    new_age = int(input("Âge du membre d'équipage : "))
    new_role = input("Rôle du membre d'équipage : ")

    if len(new_first_name) < 3 or len(new_first_name) > 15 or len(new_last_name) < 3 or len(new_last_name) > 15:
        print("Le nom et le prénom doivent contenir entre 3 et 15 caractères")
        return crew

    if new_age < 18 and new_role == "pilote":
        print("Pour être pilot il faut avoir au moins 18 ans")
        return crew
    if new_age < 25 and new_role == "technicien":
        print("Pour être technicien il faut avoir au moins 25 ans")
        return crew
    if new_age > 65 :
        print("Pour être dans l'équipage il faut avoir moins de 65 ans")
        return crew

    experience = 0
    if new_role == "technicien":
        experience = int(input("Expérience du membre d'équipage : "))
        if experience < 0:
            print("Pas possible d'avoir une expérience négative...")
            return crew
    
    for member in crew:
        if member["first_name"] == new_first_name and member["last_name"] == new_last_name:
            print("Ce membre est déjà dans l'équipage")
            return crew

    crew.append({
        "first_name": new_first_name,
        "last_name": new_last_name,
        "gender": new_gender,
        "age": new_age,
        "role": new_role,
        "experience": experience,
    })
    return crew

def remove_member(crew):
    remove_last_name = input("Nom du membre à retirer : ")
    for member in crew:
        if member["last_name"] != remove_last_name: 
            print("Ce membre n'est pas dans l'équipage")
            return crew
        else:
            crew.remove(member)
            return crew
    return crew    


def display_crew(crew):
    if crew == []:
        print("Aucun membre dans l'équipage")
    for member in crew:
        print(f"Nom : {member['last_name']} - Prénom : {member['first_name']} - Sexe : {member['gender']} - Âge : {member['age']} - Rôle : {member['role']} - Expérience : {member['experience']} ans")
    return crew

def check_crew(crew):
    if len(crew) < 2:
        print("L'équipage doit contenir au moins 2 membres")
        return crew

    pilot = False
    technician = False

    for member in crew:
        if member["role"] == "pilote" :
            pilot=True
        if member["role"] == "technicien":
            technician=True

    if pilot and technician:
        print("L'équipage est prêt pour la mission !")
    else:
        print("L'équipage n'est pas prêt")
    return crew


def random_events(crew):
    events = random.choice(["promu","démission"])
    if events == "promu":
        print("Un membre de l'équipage a été promu")
    else:
        print("Un membre de l'équipage a démissionné")
    return crew


def promote_member(crew):
    last_name = input("Nom du membre à promouvoir : ")
    first_name = input("Prénom du membre à promouvoir : ")
    for member in crew:
        if member["last_name"] != last_name or member["first_name"] != first_name:
            continue
        if member["role"] != "technicien":
            print("Ce membre n'est pas un technicien")
            return crew
        if member["experience"] < 10:
            print("Ce membre d'équipage n'a pas assez d'expérience pour être promu")
            return crew
        if member["age"] < 18 or member["age"] > 65:
            print("Ce membre d'équipage n'a pas l'âge requis pour être promu")
            return crew
        member["role"] = "pilote"
        print(f"Le membre {member['first_name']} {member['last_name']} a été promu pilote bien joué à lui")
        return crew
    print("Ce membre n'est pas dans l'équipage")
    return crew

def crew_report(crew):
    if not crew:
        print("Aucun membre dans l'équipage")
        return crew
    print(f"Nombre de membres dans l'équipage : {len(crew)}")

    roles = {}

    for member in crew:
        role_member = member["role"]
        if role_member in roles:
            roles[role_member] += 1
        else:
            roles[role_member] = 1         

    for role, count in roles.items():
        print(f"Rôle : {role} - Nombre de membres : {count}")

    for member in crew:
        if member["age"] >= 60:
            print(f"Le membre {member['first_name']} {member['last_name']} est bientôt à la retraite")

    return crew

def menu(crew):
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
                add_member(crew)
                counter_events += 1
            case "2":
                remove_member(crew) 
                counter_events += 1
            case "3":
                display_crew(crew)
                counter_events += 1
            case "4":
                check_crew(crew)
                counter_events += 1
            case "5":
                promote_member(crew)
                counter_events += 1
            case "6":
                crew_report(crew)
                counter_events += 1
            case "7":
                break
            case _:
                print("Option invalide")
        if counter_events == 5:
            random_events(crew)
            counter_events = 0

menu(crew)

    