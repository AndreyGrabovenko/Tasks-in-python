# Реализовать алгоритм задания случайных чисел. 
# Без использования встроенного генератора псевдослучайных чисел
import datetime, time
def myrandint(start,end): # генерация от -N до 0 или от 0 до N для целых чисел
    m=end
    while True:
        now = datetime.datetime.now()
        time.sleep(0.01)
        k = now.microsecond
        rNew = k%m
        while True:
            if rNew < start or rNew > end:
                now = datetime.datetime.now()
                time.sleep(0.01)
                k = now.microsecond
                rNew = k%m
            elif rNew >= start and rNew <= end:
                break
        yield rNew

for i in range(100):
    r = myrandint(970,1000)
    print(next(r),end=', ')
