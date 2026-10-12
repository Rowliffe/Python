mdp = input("Mot de passe ? \n")
count = 0 
while mdp != "python" and count < 10:
    mdp = input("Mot de passe ? \n")
    count+1
    if mdp == "python":
        print("Accès autorisé")
    else : 
        print("Accès refusé\n")
