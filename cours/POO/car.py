class Vehicule:
    def __init__(self, brand, wheel):
        self.__brand = brand
        self.__wheel = wheel
    

    def get_brand(self):
        return self.__brand

    def get_wheel(self):
        return self.__wheel

    def set_brand(self, brand):
        self.__brand = brand

    def set_wheel(self, wheel):
        self.__wheel = wheel

    def start(self):
        print(f"{self.__brand} démarre")
    
    def stop(self):
        print(f"{self.__brand} s'arrête")

    def display_info(self):
        print(f"Marque: {self.__brand}, Roues: {self.__wheel}")


class Engine:
    def __init__(self, model, power):
        self.__model = model
        self.__power = power
        self.__engine = False

    def get_model(self):
        return self.__model

    def get_power(self):
        return self.__power

    def set_model(self, model):
        self.__model = model
        
    def set_power(self, power):
        self.__power = power

    def start_engine(self):
        self.__engine = True
        print("Le moteur démarre fuck you")


class Car (Vehicule):
    def __init__(self, brand, wheel, model, color,engine_model, power):
        super().__init__(brand, wheel)
        self.__model = model
        self.__color = color
        self.__engine = Engine(engine_model,power)

    def get_model(self):
        return self.__model

    def get_color(self):
        return self.__color

    def set_model(self, model):
        self.__model = model

    def set_color(self, color): 
        self.__color = color

    def display_info(self):
        print(f"La marque de la voiture est {super().get_brand()}, le modèle est {self.__model}, la couleur est {self.__color}, le nombre de roues est {super().get_wheel()}")

    def start(self):
        self.__engine.start_engine()
     





car1 = Vehicule("Toyota", 4)
car1.display_info()
car1.start()
car1.stop()
car1.display_info()


vehicle1 = Car("Porsche", 4, "911", "Rouge","V8", 400)
vehicle1.start()
vehicle1.display_info()



