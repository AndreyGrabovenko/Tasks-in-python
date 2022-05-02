# Найти сумму чисел списка стоящих на нечетной позиции
import random
a = 0
count = 0
n = random.randint(8,15)
r = 5
lists_num = [random.randint(1,21) for i in range(r)]
for i in lists_num:
    count+=1
    if count%2!=0: 
        a += i
print(lists_num)
print(a)