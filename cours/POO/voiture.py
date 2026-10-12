class Voiture:
    def __init__(self, marque, modele, couleur):
        self.__marque = marque
        self.__modele = modele
        self.__couleur = couleur
        self.__moteur = False

    def afficher_info(self):
        print(f"Marque: {self.__marque}, Modele: {self.__modele}, Couleur: {self.__couleur}")

    def start(self):
        if self.__moteur == False:
            self.__moteur = True
            print(f"{self.__marque} {self.__modele} démarre")
        else:
            print(f"{self.__marque} {self.__modele} ne démarre pas")

    def stop(self):
        if self.__moteur == True:
            self.__moteur = False
            print(f"{self.marque} {self.modele} s'arrête")
        else:
            print(f"{self.marque} {self.modele} est déjà à l'arrêt")



    def get_marque(self):
        return self.__marque

    def get_modele(self):
        return self.__modele

    def get_couleur(self):
        return self.__couleur

    def get_moteur(self):
        return self.__moteur

    def set_marque(self, marque):
        if len(marque) >= 3 and len(marque) <= 15:
            self.__marque = marque
        else:
            print("La marque doit contenir entre 3 et 15 caractères")

    def set_modele(self, modele):
        self.__modele = modele

    def set_couleur(self, couleur):
        if self.__moteur == False :
            self.__couleur = couleur
        else:
            print("La voiture doit être à l'arrêt pour changer de couleur")

    def set_moteur(self, moteur):
        self.__moteur = moteur


voiture1 = Voiture("Ferrari", "488", "Rouge")
voiture1.set_marque("Lamborghini")
voiture1.set_modele("Aventador")
voiture1.set_couleur("Vert")
voiture1.set_moteur(True)
voiture1.afficher_info()

voiture2 = Voiture("Porshe", "GT3", "Noire")
voiture2.set_marque("Porshe")
voiture2.set_modele("GT4RS")
voiture2.start()
voiture2.set_couleur("Rouge")
voiture2.afficher_info()