import random # pip install random
import string # pip install string

# Функция для генерации случайной последовательности букв и цифр.
def generate_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

# Генерация 10 ссылок
links = ['https://discord.gift/' + generate_code() for _ in range(1000000)]

# Сохраняем ссылки в файл info.txt 
with open('C:/Users/dmitr/Desktop/PyRise-10/utilits of programm( s ) - 4/info.txt', 'w') as file:
    for link in links:
        file.write(link + '\n')