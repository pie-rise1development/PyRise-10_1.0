import random

facts =[
    "Факты о животных: Слон — единственное животное, которое не может прыгать.",
    "Факты о географии: Самая глубокая точка Земли — Марианская впадина в Тихом океане.",
    "Факты о космосе: На Венере день длиннее, чем год.",
    "Факты о человеке: У человека в среднем 100 000 волос на голове.",
    "Факты о природе: Бамбук — одно из самых быстрорастущих растений в мире.",
    "Факты о еде: Шоколад изначально использовался как напиток, а не как лакомство.",
    "Факты о языках: На Земле существует более 7000 языков.",
    "Факты о технологиях: Первое сообщение в интернете было отправлено в 1969 году.",
    "Факты о спорте: Бейсбол — один из самых популярных видов спорта в США.",
    "Факты о музыке: Самый продаваемый альбом всех времен — Thriller Майкла Джексона.",
    "Продолжительность первого выхода в космос Леоновым составила двенадцать минут.",
    "В молодости черноморские окуни в основном самки, но уже к пяти годам они радикально меняют пол.",
    "В среднем одинокие мужчины на два с половиной сантиметра ниже ростом, чем женатые.",
    "За всю историю регистрации температуры в России самой холодной зимой была зима тысяча семьсот сорокового года.",
    "Три самые богатые семьи в мире имеют больше активов, чем сорок восемь беднейших стран.",
    "Вольфганг Моцарт, один раз прослушав в Ватикане многоголосое духовное сочинение Аллегри, за ночь записал точную копию произведения.",
    "В 1991 году в Канаде на бетонном постаменте был установлен памятник топору. Вес монумента составил 7 тонн.",
    "Если у одного из однояйцевых близнецов не хватает того или иного зуба, как правило, такой же зуб отсутствует и у другого близнеца.",
    "Жирафу нужно всего 2 часа сна в день, тогда как коричневой летучей мыши - 20 часов в день.",
    "Аляска — Самый северный, Восточный, И Западный штат во всей Америке. Это также единственная часть континента, входящая в восточное полушарие.",
    "Синий кит - самое крупное млекопитающее, весящее столько же, сколько 23 слона.",
    "Глаз страуса больше, чем его мозг.",
]

def generate_random_fact():
    return random.choice(facts)

def main():
    print("Приветствую! Желаю вам набраться новой хорошей информации в моей программе 'Pie-Rise TS-Facts'! ")
    while True:
        input("Если вы хотите сгенерировать новый случайный факт, нажмите на клавишу 'Enter' и я всё сделаю за вас: ")
        fact = generate_random_fact()
        print(f'Факт: {fact}\n')

        if input("Вы хотите перезапустить программу с генерацией случайнх фактов? Напишите 'да' или 'нет': ").strip().lower() != 'да':
            print('Благодарю вас за использование моей новой разработки на Python! Желаю вам хорошего дня, удачи...')
            break

if __name__ == '__main__':
    main()