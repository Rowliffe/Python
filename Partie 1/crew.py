crew = [
    {
        "first_name": "John",
        "last_name": "Doe",
        "gender": "M",
        "age": 30,
        "role": "commander",
    },
    {
        "first_name": "Jane",
        "last_name": "Doe",
        "gender": "F",
        "age": 25,
        "role": "pilot",
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
    })
    return crew


print(add_member(crew))
