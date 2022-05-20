# Подсчитать сумму цифр в вещественном числе.

def main():
    num = input("Введите число: ")
    print(summ(num))


summ = lambda x: sum([int(i) for i in x if i.isdigit()])

main()
