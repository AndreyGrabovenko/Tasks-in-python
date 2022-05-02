# Дано число. Составить список чисел Фибоначчи,
# в том числе для отрицательных индексов. Т е для k = 8, 
# список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# Нега фибоначчи
import decimal, time
from functools import lru_cache

def dfib(n):
    decimal.getcontext().prec = 300000
    root_5 = decimal.Decimal(5).sqrt()
    phi = ((1+root_5)/2)
    a = ((phi**n)-((-phi)**-n))/root_5
    return round(a)


start_time = time.time()
# print(dfib(1000000))
print(time.time() - start_time)


# @lru_cache()
def fib(a):
    if a >= 0:
        if a == 0:
            return 0
        if a == 1 or a == 2:
            return 1
        else:
            return (fib(a-1) + fib(a-2))
    if a <= 0:
        if a == -1:
            return -1
        return int((((-1)**(a+1)) * fib(-a)))

start_time1 = time.time()
b = []
for i in range(-100,101):
    b.append(fib(i))
print(b)
print(time.time() - start_time1)
