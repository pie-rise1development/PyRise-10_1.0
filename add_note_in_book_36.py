class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Заметка/Задача которую вы хотили внести "{task}" была добавлена на сервер.')

    def view_tasks(self):
        if not self.tasks:
            print('Вы не добавили ещё ни одной задачи ')
            return
        print("Вот ваш список задач, не забудьте всё выполнить: ")
        for index, task in enumerate(self.tasks, start=1):
            print(f'{index}. {task}')
    
    def remove_task(self, index):
        try:
            removed_task = self.tasks.pop(index - 1)
            print(f'Задача "{removed_task}" была успешно удалена. ')
        except IndexError:
            print("Такого номера задачи не существует, впишите другой! ")

def main():
    manager = TaskManager()
    while True:
        print("\nВыберайте нужные для вас раздел и вперёд:")
        print("1. Добавить заметку/задачу.")
        print("2. Просмотреть уже существующие задачи/заметки.")
        print("3. Удалить ненужный текст.")
        print("4. Покинуть программу.")

        choice = input("Выбирайте любой из заданных пунктов и вписывайте его цифру здесь: ")

        if choice == '1':
            task = input("Напишите задачу, которую вы хотите внести на сервер: ")
            manager.add_task(task)
        elif choice == '2':
            manager.view_tasks()
        elif choice == '3':
            index = int(input("Напишите номер задачи которую вы хотели-бы удалить навсегда: "))
            manager.remove_task(index)
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Упссс... Извините, но такого раздела не существует, или вы не правильно вписали нужные вам параметры, попробуйте ещё раз через 5 минут!")

if __name__ == "__main__":
    main()