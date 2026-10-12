vitesse = int(input("Entrez votre vitesse : \n"))

if vitesse >= 90 :
    print(" Excès vitesse dangereux")
elif vitesse > 50 and vitesse < 70:
    print("Vitesse OK")
else : 
    print("OK")