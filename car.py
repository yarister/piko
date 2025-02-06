class Car:
    def __init__(self, year, manufacturer, model, fuel_consumption, dealer_price):
        self.year = year
        self.manufacturer = manufacturer
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.dealer_price = dealer_price
        self.mileage = 0

    def drive(self):
        print(f"Я авто марки {self.model}, їду по справам господаря")

    @property
    def category(self):
        return "Крутяк" if self.dealer_price > 15000 else "тачелла"
