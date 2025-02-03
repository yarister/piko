import requests

# URL PDF-файла
pdf_url = "https://chtyvo.org.ua/authors/Falkovych_Hryhorii/Smyk-tyndyk.pdf"

# Запрос к серверу
response = requests.get(pdf_url)

# Проверяем, успешно ли скачан файл
if response.status_code == 200:
    with open("Smyk-tyndyk.pdf", "wb") as file:
        file.write(response.content)
    print("✅ PDF-файл успешно сохранен как 'Smyk-tyndyk.pdf'")
else:
    print("❌ Ошибка загрузки PDF:", response.status_code)
