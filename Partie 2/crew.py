class Person:
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def introduce_yourself(self):
        return f"Je m'appelle {self.first_name} {self.last_name}, je suis un/une {self.gender} de  {self.age} ans "

class Operator(Person):
    def __init__(self, first_name, last_name, gender, age, role):
        super().__init__(first_name, last_name, gender, age)
        self.role = role
        self.experience = 0

    def act(self):
        if self.role == "technicien":
            print(f"{self.first_name} {self.last_name} nettoie le vaisseau.")
        elif self.role == "pilote":
            print(f"{self.first_name} {self.last_name} pilote le vaisseau.")
        else:
            print(f"{self.first_name} {self.last_name} effectue sa tâche.")

    def gain_experience(self):
        self.experience += 1



class Mentalist(Person):
    def __init__(self, first_name, last_name, gender, age):
        super().__init__(first_name, last_name, gender, age)
        self.mana = 100

    def act(self, operator):
        if self.mana < 20:
            print(f"{self.first_name} n'a pas assez de mana pour influencer {operator.first_name}")
            return
        self.mana -= 20
        print(f"{self.first_name} {self.last_name} force {operator.first_name} {operator.last_name} à agir")
        operator.act()

    def recharge_mana(self):
        self.mana += 50
        if self.mana > 100:
            self.mana = 100


class Spaceship:
    def __init__(self, name, shipType, condition):
        self.name = name
        self.shipType = shipType
        self.crew = []
        self.condition = condition

    def add_member(self, member):
        if len(self.crew) >= 10:
            print("Le vaisseau a déjà 10 membres")
            return
        self.crew.append(member)

    def check_preparation(self):
        pilot = False
        technician = False
        mentalist_ready = False

        for member in self.crew:
            if type(member) == Operator:
                if member.role == "pilote":
                    pilot = True
                if member.role == "technicien":
                    technician = True
            if type(member) == Mentalist and member.mana >= 50:
                mentalist_ready = True

        if pilot == True and technician == True and mentalist_ready == True:
            return True
        else:
            return False



class Fleet:
    def __init__(self, name):
        self.name = name
        self.spaceships = []

    def add_spaceship(self, spaceship):
        if len(self.spaceships) >= 15:
            print("La flotte a déjà 15 vaisseaux")
            return
        self.spaceships.append(spaceship)

    def statistics(self):
        total_members = 0
        roles = {}
        total_experience = 0
        nombre_operators = 0

        for ship in self.spaceships:
            for member in ship.crew:
                total_members += 1
                if type(member) == Operator:
                    nombre_operators += 1
                    total_experience += member.experience
                    role_member = member.role
                    if role_member in roles:
                        roles[role_member] += 1
                    else:
                        roles[role_member] = 1
        print(f"Nombre total de membres : {total_members}")

        for role, count in roles.items():
            print(f"Rôle : {role} - Nombre de membres : {count}")

        if nombre_operators == 0:
            print("Niveau moyen d'expérience : 0")
        else:
            print(f"Niveau moyen d'expérience : {total_experience / nombre_operators}")
