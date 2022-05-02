# Сообщить в какой четверти координатной плоскости
# или на какой оси находится точка с координатами Х и У 

def main():
    num1 = input("Введите координату X: ")
    num2 = input("Введите координату Y: ")
    bool = True
    while bool:
        try:
            X = float(num1)
            Y = float(num2)
        except ValueError:
            print('Это не число!')
            num1 = input("Введите координату X: ")
            num2 = input("Введите координату Y: ")
        else:
            bool = False
    plane(X,Y)
def plane(x, y):
    if x == 0 and y == 0: print("центр плоскости") 
    elif x > 0 and  y > 0: print("Первая четверть") 
    elif x < 0 and  y > 0: print("Вторая четверть")
    elif x < 0 and  y < 0: print("Третья четверть") 
    elif x > 0 and  y < 0: print("Четвёртая четверть")
    elif x == 0 and  (y > 0 or y < 0): print("точка находится на оси Y") 
    elif y == 0 and (x > 0 or x < 0): print("точка находится на оси X")
main()