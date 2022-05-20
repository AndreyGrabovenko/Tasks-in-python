# Для натурального n создать словарь индекс-значение, 
# состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def main():
    num = input("Введите число: ")
    bool = True
    while bool:
        try:
            number = int(num)
        except ValueError:
            print('Повторите ввод целочисленного числа!')
            num = input("Введите число: ")
        else:
            if number < 0:
                print('Число не может быть отрицательмым')
                num = input("Введите число: ")
            else:
                bool = False
    print(n(number))


n = lambda x: {i: 3 * i + 1 for i in range(1, x + 1)}

main()
