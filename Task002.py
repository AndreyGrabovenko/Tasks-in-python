# Найти максимальное из пяти чисел

num = input('Введите числа разделёные пробелом: ')
numbers = []
for i in num.split(' '):
    numbers.append(int(i))
print('Максимальное число: ', max(numbers))