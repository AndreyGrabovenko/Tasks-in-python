# Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

import random
from functools import reduce


def main():
    num = input('Введите число: ')
    bool = True
    while bool:
        try:
            number = int(num)
        except ValueError:
            print('Число ведено неверно!')
            num = input('Введите число: ')
        if number == 0: return []
        if number < 0:
            print('Число не может быть отрицательмым')
            num = input("Введите число: ")
        else: bool = False
    negative_meaning = number * (-1)
    lists = lambda: [i for i in range(negative_meaning, number)]
    amount_of_elements = random.randrange(1, number * 2 - 1)
    element_index = lambda: set(random.randrange(number * 2) for i in range(amount_of_elements))
    with open(r"file.txt", 'w') as f: f.writelines(str(i)+'\n' for i in element_index())
    with open(r"file.txt") as f: list_file = [int(i.strip('\n')) for i in f]
    list = lists()
    element_search = lambda: [list[i] for i in list_file]
    print(f'исходный масив: {list} \nискомые позиции: {list_file}\nпроизведение элементов {reduce(lambda x, y: x * y, element_search())}')


main()
