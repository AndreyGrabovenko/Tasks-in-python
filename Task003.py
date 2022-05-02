# Вывести на экран числа от -N до N

def main():
    num1 = input('Введите целочисленное число 1: ')
    num2 = input('Введите целочисленное число 2: ')
    bool = True
    while bool:
        try:
            numbers1 = int(num1)
            numbers2 = int(num2)
        except ValueError:
            print('Введите натуральное число!')
            num1 = input('Введите целочисленное число 1: ')
            num2 = input('Введите целочисленное число 2: ')
        else:
            bool = False
            
            
    if numbers1 < numbers2:
        for i in range(numbers1, numbers2 + 1):
            print(i,end=' ')
    else:
        for i in range(numbers1, numbers2 -1, -1):
            print(i,end=' ')
main()