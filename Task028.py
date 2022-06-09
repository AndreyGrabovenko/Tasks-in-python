# Найти корни квадратного уравнения Ax² + Bx + C = 0
# a. Математикой
# b. Используя дополнительные библиотеки*
from My_square import my_square
import math
def main():
    print("\nВведите коэффициенты для уравнения: Ax² + Bx + C = 0\n")
    num_A = input("Введите число A: ")
    num_B = input("Введите число B: ")
    num_C = input("Введите число C: ")

    bool = True
    while bool:
        try:
            A = float(num_A)
            B = float(num_B)
            C = float(num_C)

        except ValueError:
            print('\nВведённая вами число не соотвествует параметрам числа!\n')
            num_A = input("Введите число A: ")
            num_B = input("Введите число B: ")
            num_C = input("Введите число C: ")
        else:
            bool = False
    D = pow(B,2)-4*A*C
    print(f'\nДискриминант  = {D:.5}\n')
    if D < 0:
        print('Корней нет!\n')
    elif D == 0:
        x = (-B)/(2*A)
        print(f'Имеется один корень: {x:.2}\n')
    elif D > 0:
        x1 = (-B + my_square.square_root(D))/(2 * A) # использовал собственный модуль 
        x2 = (-B - my_square.square_root(D))/(2 * A) # для вывода числа из квадратного корня
        print(f'Имеется два корня:\n')
        print(f'x1 = {x1:.3} \nx2 = {x2:.3}\n')
        
        x3 = (-B + math.sqrt(D))/(2 * A) # использовал встроенный модуль 
        x4 = (-B - math.sqrt(D))/(2 * A) # для вывода числа из квадратного корня
        print(f'Имеется два корня:\n')
        print(f'x3 = {x3:.3} \nx4 = {x4:.3}\n')
main()
