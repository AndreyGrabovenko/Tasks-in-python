# Указав номер четверти прямоугольной системы координат, 
# показать допустимые значения координат для точек этой четверти

def main():
    num = input("Введите номер четверти от 1 до 4: ")
    bool = True
    while bool:
        try:
            number = int(num)
        except ValueError:
            print('Это не номер четверти!')
            num = input("Введите номер четверти от 1 до 4: ")
        if number <= 0 or number > 4:
            print('Это не номер четверти!')
            num = input("Введите номер четверти от 1 до 4: ")
        else:
            bool = False
    plane(number)
def plane(number):
    if number == 1: print("диапозон от X до Y")
    elif number == 2: print("диапозон от -X до Y")
    elif number == 3: print("диапозон от -X до -Y")
    elif number == 4: print("диапозон от X до -Y")
main()