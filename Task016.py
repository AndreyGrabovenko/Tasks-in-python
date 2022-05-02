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
    sum = 0
    for i in range(1, number+1):
        sum += (1+1/number)**number
    print(format(sum, '.3f'))
main()