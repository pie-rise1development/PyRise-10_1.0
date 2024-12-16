import random
from faker import Faker

def generate_fake_identity():
    fake = Faker('ru_RU') # Использование русской локали.
    first_name = fake.first_name()
    age = random.randint(18, 55)
    job = fake.job()
    last_name = fake.last_name()
    patronymic = fake.first_name_male() + 'ович' # Генерация отчества для мужчин.
    phone_number = fake.phone_number()
    card_number = fake.credit_card_number(card_type='mastercard')
    birth_date = fake.date_of_birth(minimum_age=18, maximum_age=55)
    payment_system = random.choice(['Visa', 'MasterCard', 'Mir', 'American Express'])
    expiration_date = fake.credit_card_expire()
    address = fake.address().replace("\n", ", ")
    user_agent = fake.user_agent()
    inn = ''.join([str(random.randint(0, 9)) for _ in range(10)]) # Генерация ИНН.
    orgn = fake.random_int(min=100000000, max=999999999) # 9 цифр для ОРГН.
    country = fake.country()

    identity = {
        "Имя": first_name,
        "Фамилия": last_name,
        "Отчество": patronymic,
        "Место работы": f'<<{job}>>',
        "Телефон": phone_number,
        "Адрес": address,
        "Номер карты": card_number,
        "Срок действия": expiration_date,
        "Дата рождения": birth_date.strftime('%d-%m-%Y'),
        "Юзерагент": user_agent,
        "Платёжная система": payment_system,
        "Возраст": age,
        "ИНН": inn,
        "ОРГН": orgn,
        "Страна": country
    }

    return identity

if __name__ == "__main__":
    fake_identity = generate_fake_identity()
    for key, value in fake_identity.items():
        print(f"{key}: {value}")