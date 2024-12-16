def get_horoscope(sign):
    horoscopes = {
        "Овен": "Вам предстоит вступить в нелегкую борьбу с сильным противником. Профессиональное противостояние осложняется личной антипатией, выбраться из сложившейся ситуации без потерь очень трудно. Поступающие деловые предложения подкупают своей новизной, но все же не настолько хороши, чтобы быть принятыми немедленно. Если речь идет о деньгах, торгуйтесь: вы получите больше, чем предлагают сначала.",
        "Телец": "Удачный день для представителей знака, занятых интеллектуальным трудом. Тельцы блестяще справляются с решением сложных задач. Окружающие не всегда понимают вас с полуслова, но вы достаточно терпеливы и не выходите из себя, даже если приходится давать объяснения неоднократно. Неплохой день для проведения переговоров, однако будьте настороже: окружающие попытаются получить от вас информацию, которую вы предпочли бы сохранить в тайне.",
        "Близнецы": "День подходит для посещения светских мероприятий. На них вас непременно заметят – в том числе и благодаря яркому наряду.",
        "Рак": "В этот день можно добиться замечательных результатов, приложив для этого лишь самые скромные усилия. Воспользуйтесь благоприятным моментом, чтобы воплотить в жизнь все, что было задумано в последнее время. Энергии у вас много, переутомление вам не грозит.",
        "Лев": "Одна из главных задач этого дня – сохранить хорошие отношения с окружающими. Постарайтесь не нажить себе врагов, никого не обидеть, никому не дать повода затаить злобу. В середине дня вам может потребоваться помощь; обращайтесь только к тем, в чьем расположении уверены. Не рискуйте ни своими, ни чужими деньгами.",
        "Дева": "Нейтральный день, как нельзя лучше подходящий для того, чтобы подводить итоги и делать выводы. Вам удается сконцентрироваться на главном, ни один важный факт не ускользнет от вашего внимания. Могут раздражать внимание и не всегда тактичные замечания родственников, однако ссор вы не допустите.",
        "Весы": "Вы решительны, нетерпеливы, часто говорите и действуете, не подумав. В результате день оказывается полным разнообразных происшествий, вспоминать о которых потом будет очень весело. Пока же вы переживаете, нервничаете, беспокоитесь – словом, не даете покоя ни себе, ни окружающим.",
        "Скорпион": "Ваши желания многочисленны и разнообразны, и тем обиднее, что, когда до их реализации, кажется, рукой подать, обстоятельства непреодолимой силы в корне меняют ситуацию. От этого дня не следует ожидать многого, тогда разочарование не причинит вам боли.",
        "Стрелец": "Все идет не так, вам крайне трудно держать себя в руках. Раздражение и недовольства копятся, чтобы затем вырваться наружу в самый неподходящий момент. В результате возникают конфликты с людьми, с которыми вы совсем не хотели ссориться. Сгоряча вы говорите много лишнего, и позже об этом придется жалеть.",
        "Козерог": "День приятного и интересного общения, встреч, которые оставят самое лучшее впечатление и положат начало серьезным отношениям. В такой день легко потерять голову от человека, которого вы видите впервые; возможна настоящая любовь с первого взгляда. Особенно повезет некоторым представителям знака – сбудутся их тайные мечты.",
        "Водолей": "Удачный день, в течение которого вы не раз сможете проявить находчивость и сообразительность, удивить начальство своими блестящими идеями, произвести отличное впечатление на потенциальных помощников и союзников. Возможны денежные поступления, не исключены ценные подарки от людей, которым вы когда-то помогли.",
        "Рыбы": "Не поддаться на провокации трудно, но у вас это все же получится. Проявите твердость, не идите на поводу у окружающих, не позволяйте каждому встречному лентяю и бездельнику сесть вам на шею. В этот день вам многие свои проблемы придется решать самостоятельно, но это не повод заниматься еще и чужими делами."
    }

    return horoscopes.get(sign, "Знак зодиака не найден.")


def main():
    print("Приветствую, дорогой друг! Ты присоединился к еженедельному обновлению гороскопа, желаю тебе удачи, узнай то, что тебя ждёт сегодня...")

    sign = input("Введите в поле свой знак зодиака: ")

    horoscope = get_horoscope(sign)

    print(f"Вот, какой гороскоп на сегодня вас ждёт: {horoscope}")


if __name__ == '__main__':
    main()