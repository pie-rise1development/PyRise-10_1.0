import time


def time_of_function(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time()
        result = t2 - t1
        print(f'Работа данного проекта была подсчитана, время выполнения находится здесь => {result}')
    return wrapper


@time_of_function
def func_one():
    my_list = [i for i in range(1, 1000000)]


@time_of_function
def func_two():
    my_list = [i for i in range(1, 1000000)]


func_one()
func_two()

print('-')
print('-')
print('-')
name = input('Вам понравилась данная функция?: ')
print('Ваш отзыв о проекте:', name)