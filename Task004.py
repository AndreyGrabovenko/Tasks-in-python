# Показать первую цифру дробной части числа

def main():
    num = input('Введите дробное число: ')
    bool = True
    while bool:
        try:
            number = float(num)
        except ValueError:
            print('Введите дробное число!')
            num = input('Введите дробное число: ')
        else:
            bool = False
    print(int(number*10)%10)
main()