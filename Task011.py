# Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.
import math


def main():
    num = input("Введите число: ")
    bool = True
    while bool:
        try:
            number = int(num)
        except ValueError:
            print('Повторите ввод целого числа!')
            num = input("Введите число: ")
        else:
            if number < 0:
                print('Число не может быть отрицательмым')
                num = input("Введите число: ")
            else:
                bool = False
    print(lists(number))


lists = lambda x: [format(math.pow(-3, i), '.0f') for i in range(x)]

main()
