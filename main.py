

from prices import prices
from phrases import phrases

def main():
    print("Вітаємо в ресторані 'Дача'!")
    name = input("Як вас звати? ")
    print(f"Привіт, {name}! Сьогодні у нас 15% знижка на всі страви!")

    print("\nМеню:")
    for dish, price in prices.items():
        print(f"{dish} - {price} грн за порцію")

    print("\nНаші рекомендації:")
    for dish, phrase in phrases.items():
        print(f"{dish}: {phrase}")

    print("\nВведіть кількість порцій для кожної страви (0, якщо не хочете замовити):")
    order = {}
    for dish in prices.keys():
        while True:
            try:
                quantity = int(input(f"{dish}: "))
                if quantity >= 0:
                    order[dish] = quantity
                    break
                else:
                    print("Кількість повинна бути 0 або більше.")
            except ValueError:
                print("Будь ласка, введіть число.")

    total = 0
    print("\nВаше замовлення:")
    for dish, quantity in order.items():
        if quantity > 0:
            cost = quantity * prices[dish]
            print(f"{dish}: {quantity} порцій x {prices[dish]} грн = {cost} грн")
            total += cost

    discount = total * 0.15
    final_total = total - discount

    print("\nЧек:")
    print(f"Загальна сума: {total} грн")
    print(f"Знижка (15%): {discount:.2f} грн")
    print(f"До сплати: {final_total:.2f} грн")
    print(f"Дякуємо, {name}, за ваше замовлення! Приходьте ще!")

if __name__ == "__main__":
    main()
