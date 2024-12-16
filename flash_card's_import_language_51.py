import random

class Flashcard:
    def __init__(self, word, translation):
        self.word = word
        self.translation = translation

class FlashcardApp:
    def __init__(self):
        self.flashcards = []

    def add_flashcard(self, word, translation):
        self.flashcards.append(Flashcard(word, translation))
        print(f'Флеш-карточка "{word}" -> "{translation}" добавлена.')

    def study(self):
        if not self.flashcards:
            print("Нет доступных флеш-карточек.")
            return
        
        random.shuffle(self.flashcards)
        for card in self.flashcards:
            answer = input(f'Переведите слово "{card.word}": ')
            if answer.lower() == card.translation.lower():
                print("Правильно!")
            else:
                print(f"Неправильно. Правильный ответ: {card.translation}")

def main():
    app = FlashcardApp()
    while True:
        print("\nВыберите действие:")
        print("1. Добавить флеш-карточку")
        print("2. Изучать слова")
        print("3. Выйти")

        choice = input("Выш выбор: ")

        if choice == '1':
            word = input("Введите слово: ")
            translation = input("Введите перевод слова: ")
            app.add_flashcard(word, translation)
        elif choice == '2':
            app.study()
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор, попробуйте снова.")

if __name__ == '__main__':
    main()