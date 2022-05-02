# Вычислить число PI c заданной точностью d
# Пример: при d = 0.001,  = 3.141. 10-1d≤10-10
from decimal import *
from math import factorial
 
def chudnovsky(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(-1)**k) * (Decimal(factorial(6 * k)) /
                                  ((factorial(k)**3) * (factorial(3 * k))) * 
                                  (13591409 + 545140134 * k) / (640320**(3 * k)))
        k += 1
    pi = pi * Decimal(10005).sqrt() / 4270934400
    pi = pi**(-1)
    return pi
 
 
def chudnovsky2(n):
    pi = Decimal(13591409)
    ak = Decimal(1)
    k = 1
    while k < n:
        ak *= -Decimal((6*k-5)*(2*k-1)*(6*k-1))/Decimal(k*k*k*26680*640320*640320)
        val = ak*(13591409 + 545140134*k)
        pi += val
        k += 1
    pi = pi * Decimal(10005).sqrt()/4270934400
    pi = pi**(-1)
    return pi
 
n = 100
getcontext().prec = n
print(chudnovsky(n))
print(chudnovsky2(n))
