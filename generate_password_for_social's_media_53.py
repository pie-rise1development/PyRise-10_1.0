import random

password = ""
symbols = "abcdefghijklmnopqrstuvwxyz"

numbers = "0123456789"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special = "!@#$%^&*()_+=-<>?"

lenght = int(input("Введите размер вашего пароля: "))
is_uppercase = input("Использовать верхний регистр (да/нет): ")
is_number = input("Использовать цифры (да/нет): ")
is_special = input("Использовать специальные символы (да/нет): ")

if is_uppercase == "да":
    symbols += uppercase

if is_special == "да":
    symbols =+ special
    
for index in range(lenght):
    password += random.choice(symbols)

print("Ваш пароль: " + password)