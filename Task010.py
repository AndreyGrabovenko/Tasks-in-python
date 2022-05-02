# Найти расстояние между двумя точками пространства
import math
def main():
    x_1 = input("Введите координаты x1: ")
    x_2 = input("Введите координаты x2: ")
    y_1 = input("Введите координаты y1: ")
    y_2 = input("Введите координаты y2: ")
    z_1 = input("Введите координаты z1: ")
    z_2 = input("Введите координаты z2: ")
    bool = True
    while bool:
        try:
            x1 = float(x_1)
            x2 = float(x_2)
            y1 = float(y_1)
            y2 = float(y_2)
            z1 = float(z_1)
            z2 = float(z_2)
        except ValueError:
            print('Это не число!')
            x_1 = input("Введите координаты x1: ")
            x_2 = input("Введите координаты x2: ")
            y_1 = input("Введите координаты y1: ")
            y_2 = input("Введите координаты y2: ")
            z_1 = input("Введите координаты z1: ")
            z_2 = input("Введите координаты z2: ")
        else:
            bool = False
    distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) + math.pow(z2 - z1, 2));
    print(f"Расстояние между двумя точками в пространстве равно {format(distance, '.3f')}")
main()