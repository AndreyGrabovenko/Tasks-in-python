# Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.
import math
def main():
    num = input("Введите число: ")
    bool = True
    lists = []
    while bool:
        try:
            number = int(num)
        except ValueError:
            print('Повторите ввод целого числа!')
            num = input("Введите число: ")
        else:
            bool = False
    for i in range(number+1): lists.append(format(math.pow(-3,i), '.0f'))
    for i in lists:
        print(i, end=' ')
main()