from translate import Translator

translator = Translator(from_lang="eng", to_lang="ru")
text =str(input("Введите текст который хотите перевести: "))

end_text = translator.translate(text)
print("Ваш перевод:", end_text)
print("-")
print("-")
print("-")
print("P.S.S: Если вы используете данный переводчик на данный момент, то знайте, именно он был сделан человеком под именем Пирожок с Рисом - LiFE!")

