# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, 
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.
from posixpath import split
import random

# N = int(input('Введите количество чисел: '))

with open('natural_numbers', 'w') as f:
    for i in range(11):
        x = str(random.randint(1, 11)) + ' '
        f.write(x)
A = []
f = open('natural_numbers', 'r')
A = f.readline()
print(A)
f.close()
A = A.split()
for i in range(1,len(A)):
    if int(A[i]) - 1 == int(A[i - 1]):
        print(f"{int(A[i])} - 1 = {int(A[i - 1])}")
    else:
        print(i)
        break
