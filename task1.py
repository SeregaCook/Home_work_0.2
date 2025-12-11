# ===== Задание 1: Транспортные средства =====

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} запускается.")


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def honk(self):
        print(f"{self.brand} {self.model}: Бип-бип!")


class Bicycle(Vehicle):
    def __init__(self, brand, model, gears):
        super().__init__(brand, model)
        self.gears = gears

    def ring_bell(self):
        print(f"{self.brand} {self.model}: Дзынь-дзынь!")


# Демонстрация
car = Car("Toyota", "Camry", "Бензин")
bike = Bicycle("Trek", "FX 3", 21)

car.start()
car.honk()

bike.start()
bike.ring_bell()
