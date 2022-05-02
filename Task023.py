# Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]
import math
a = []
num = [2, 3, 4, 5, 6]
count = 0
x = math.ceil(len(num)/2)
for i in num:
    a.append(num[count] * num[(count+1)*(-1)])
    count += 1
    if x == count: break
print(a)