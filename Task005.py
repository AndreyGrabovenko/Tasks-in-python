# Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

def main():
    num = input("Введите число: ")
    bool = True
    while bool:
        try:
            numbers = int(num)
        except ValueError:
            print('Введите правильно число!')
            num = input("Введите число: ")
        else:
            bool = False
    if (((numbers % 5 == 0 and numbers % 10 == 0) or numbers % 15 == 0) and numbers % 30 != 0):
        print('Число кратно 5, 10 или 15 но не 30')
    else:
        print('число не кратно')
main()