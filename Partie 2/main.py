import crew

person1 = crew.Person("John", "Doe", "homme", 30)
pilote = crew.Operator("Jane", "Doe", "femme", 25, "pilote")
technicien = crew.Operator("Gaal", "Dornick", "femme", 28, "technicien")
mentaliste = crew.Mentalist("Hari", "Seldon", "homme", 40)

print(person1.introduce_yourself())
print(pilote.introduce_yourself())
print(mentaliste.introduce_yourself())

print(pilote.role)
print(pilote.experience)
pilote.act()
pilote.gain_experience()
print(pilote.experience)

technicien.act()
technicien.gain_experience()
technicien.gain_experience()

print(mentaliste.mana)
mentaliste.act(technicien)
print(mentaliste.mana)
mentaliste.recharge_mana()
print(mentaliste.mana)

ship1 = crew.Spaceship("Enterprise", "guerre", "opérationnel")
ship1.add_member(person1)
ship1.add_member(pilote)
ship1.add_member(technicien)
ship1.add_member(mentaliste)

print(ship1.name)
print(ship1.shipType)
print(ship1.condition)
print(ship1.check_preparation())

for member in ship1.crew:
    print(member.first_name, member.last_name)

fleet = crew.Fleet("Fondation")
fleet.add_spaceship(ship1)
print(fleet.name)
fleet.statistics()
