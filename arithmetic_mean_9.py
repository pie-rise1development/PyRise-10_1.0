def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def main():
    numbers = input("Впишите числа, из которых вы хотите выделить среднее арифметическое ( разделяйте числа которые вы хотите ввести пробелом! ): ")
    num_list = [float(num) for num in numbers.split()]

    average = calculate_average(num_list)

    print(f"Я вычислил среднее арифметическое заданных вами чисел, получился вот такой ответ: {average}")

if __name__ == "__main__":
    main()