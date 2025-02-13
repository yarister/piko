class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"Транспортний засіб: {self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors

    def info(self):
        return f"Автомобіль: {self.brand} {self.model}, Дверей: {self.num_doors}"

class Bike(Vehicle):
    def __init__(self, brand, model, bike_type):
        super().__init__(brand, model)
        self.bike_type = bike_type

    def info(self):
        return f"Велосипед: {self.brand} {self.model}, Тип: {self.bike_type}"

class Truck(Vehicle):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity

    def info(self):
        return f"Вантажівка: {self.brand} {self.model}, Вантажопідйомність: {self.capacity} кг"
