# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

def main():
    num = input("Введите число: ")
    bool = True
    while bool:
        try:
            number = int(num)
        except ValueError:
            print('Число введено неверно!')
            num = input("Введите число: ")
        else:
            bool = False
    print(factotial(number))


factotial = lambda b: [(lambda a, i: a(a, i))(lambda a, i: i * a(a, i - 1) if i > 0 else 1, i) for i in range(1, b + 1)]

main()
