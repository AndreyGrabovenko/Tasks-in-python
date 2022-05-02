# В заданном списке вещественных чисел найдите разницу 
# между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random, math
a = [1.1, 1.2, 3.1, 5, 10.01]
b = []
# for i in range(10): a.append(random.uniform(1.01,10.5))
for i in a: b.append(int((i*100)%100))
min1 = min(b)
max1 = max(b)
for i in a: print(format(i, '.4f'), end=' ')
print()
print('max', format((max1/100), '.2f'))
print('min', format((min1/100), '.2f'))
print("разница между максимальным и минимальным элементом: ", format(((max1 - min1)/100), '.2f'))