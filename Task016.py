# Задать список из n чисел последовательности (1+(1/n))**n и вывести на экран их сумму

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
    print(suma(number))


suma = lambda x: sum([(1+(1/i))**i for i in range(1, x+1)])

main()
