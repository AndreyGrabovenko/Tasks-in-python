# Подсчитать сумму цифр в вещественном числе.

def main():
    num = input("Введите число: ")
    bool = True
    while bool:
        try:
            number = float(num)
        except ValueError:
            print('Число введено неверно!')
            num = input("Введите число: ")
        else:
            bool = False
    sum = 0
    count = 0
    for i in str(number):
        if num[count] != '.':
            try:
                sum += int(num[count])
                count +=1
            except ValueError:
                print('Число введено неверно!')
                num = input("Введите число: ")
        else:
            count +=1
            continue
    print(sum)
main()