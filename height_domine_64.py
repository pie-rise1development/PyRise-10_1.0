import whois

def domain_lookup(domain_name):
    try:
        domain_info = whois.whois(domain_name)

        print("Информация о домене:")
        print("---------------------")
        print(f"Доменное имя: {domain_info.domain_name}")
        print(f"Регистратор: {domain_info.registar}")
        print(f"Дата создания: {domain_info.creation_date}")
        print(f"Дата истечения: {domain_info.expiration_date}")
        print(f"Контакты регистратора: {domain_info.emails}")

        if domain_info.name_servers:
            print(f"DNS-серверы: {', '.join(domain_info.name_servers)}")
        else:
            print("DNS-серверы: Неизвестно")

    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    domain_name = input("Введите доменное имя (например, example.com): ")
    domain_lookup(domain_name)