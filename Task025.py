# Написать программу преобразования десятичного числа в двоичное

n  = int(input('Введите число: '))
print(f'{n:b}')
b = ''
while n > 0:
    b = str(n%2)+b
    n = n//2
print(b)