import requests
import json


json_url = "http://api.open-notify.org/astros.json"


response = requests.get(json_url)


if response.status_code == 200:
    data = response.json()
    with open("astros.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    print("✅ JSON-данные успешно сохранены в 'astros.json'")
else:
    print("❌ Ошибка загрузки JSON:", response.status_code)
