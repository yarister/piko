from car import Car

auto1 = Car(2022, "Toyota", "Camry", 7.5, 20000)
auto2 = Car(2018, "Ford", "Focus", 6.2, 12000)

auto2.mileage = 50000

auto1.drive()

print(auto1.category)  # Крутяк
print(auto2.category)  # тачелла
f