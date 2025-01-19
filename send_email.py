from jinja2 import Environment, FileSystemLoader
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Дані про автомобіль
car_data = {
    "car_name": "Audi A8",
    "brand": "Audi",
    "model": "A8",
    "year": 2023,
    "price": 45000,
    "seats": 5,
    "options": [
        "Шкіряний салон",
        "Система підігріву сидінь",
        "Система масажу сидінь",
        "Система безключового доступу (Keyless Entry)",
        "Apple CarPlay/Android Auto"
    ],
    "car_class": "Преміум автомобіль" if 45000 > 30000 else "Доступний автомобіль"
}

# Рендеринг шаблону
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('car_email_template.html')
html_content = template.render(car_data)

# Налаштування листа
sender_email = "yaroslav.kirnos@gmail.com"
receiver_email = "yaroslav.kirnos@gmail.com"
subject = f"Реклама автомобіля: {car_data['car_name']}"

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(html_content, 'html'))

# Відправка листа через SMTP
try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, "12k01y09AAAA")  
        server.send_message(msg)
        print("Лист успішно надіслано!")
except Exception as e:
    print(f"Помилка при відправці: {e}")
