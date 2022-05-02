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
    lists = [1]
    for i in range(1, number+1):
        lists.append(lists[i-1] * (i))
    del lists[0]
    print(lists)
main()