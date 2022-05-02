# Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число
import os

from nbformat import write
def main():
    num1 = input('Введите число 1: ')
    num2 = input('Введите число 2: ')
    bool = True
    while bool:
        try:
            numbers1 = int(num1)
            numbers2 = int(num2)
        except ValueError:
            print('Число ведено неверно!')
            num1 = input('Введите число 1: ')
            num2 = input('Введите число 2: ')
        if numbers1 == 0:
            print('Первое число не может начинаться с 0!')
            num1 = input('Введите число 1: ')
            num2 = input('Введите число 2: ')
        else:
            bool = False
    lists = []
    if numbers1 < numbers2:
        for i in range(numbers1, numbers2 + 1): lists.append(i)
    else:
        for i in range(numbers1, numbers2 -1, -1): lists.append(i)
    file = open(r'F:\програмирование\Обучение Python\EX\file\file.txt', 'w')
    for i in lists: file.write(str(i) + '\n')
    file.close()
    file1 = open(r'F:\програмирование\Обучение Python\EX\file\file.txt', 'r')
    d = []
    for i in file1:
        r = i.rstrip('\n')
        d.append(int(r))
    file1.close()
    count = 1
    work = d[0]
    for i in range(len(d)-1):
        if d[count] == 0:
            count+=1
            continue
        else:
            work = work * d[count]
            count+=1
    print(work)
main()