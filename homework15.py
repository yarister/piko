car_info = {
    "модель": "Toyota C-HR Гібрид",
    "ціна": 1905290,  # в гривнях
    "ціна": 1905290,  # в гривнях
    "робочий_об'єм_двигуна": 2.0,  # в літрах
    "повна_маса": None,  # інформація відсутня
    "максимальна_швидкість": None,  # інформація відсутня
    "особливості_інтер'єру": [
        "Преміум матеріали обробки",
        "Сучасна мультимедійна система",
        "Клімат-контроль",
        "Підігрів сидінь"
    ],
    "багажне_відділення": {
        "об'єм_багажника": None,  # інформація відсутня
        "об'єм_багажника_зі_складеними_сидіннями": None  # інформація відсутня
    }
}

# Додавання інформації про максимальну дозволену масу причепа з гальмами
car_info["максимальна_дозволена_маса_причепа_з_гальмами"] = None  # інформація відсутня

# Отримання інформації зі словника
назва_авто = car_info["модель"]
ціна_авто = car_info["ціна"]
перша_опція_інтер'єру = car_info["особливості_інтер'єру"][0]
об'єм_багажника_зі_складеними_сидіннями = car_info["багажне_відділення"]["об'єм_багажника_зі_складеними_сидіннями"]

print(f"Назва авто: {назва_авто}")
print(f"Ціна авто: {ціна_авто}")
print(f"Перша опція інтер'єру: {перша_опція_інтер'єру}")
print(f"Об'єм багажника зі складеними сидіннями: {об'єм_багажника_зі_складеними_сидіннями}")
