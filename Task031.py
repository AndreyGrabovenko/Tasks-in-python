# Составить список простых множителей натурального числа N
def main():
    num = input("Введите число: ")
    bool = True
    while bool:
        try:
            number = int(num)
        except ValueError:
            print('\nВведённая вами число не соотвествует параметрам числа!\n')
            number = input("Введите число: ")
        else:
            bool = False
    print(Factor(number))
def Factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else: d += 1
    if n > 1:
        Ans.append(n)
    return Ans
main()

# import gmpy2

# def is_prime(num):
#   return gmpy2.is_prime(num) if num > 0 else False # проверка является ли число простым

# print(is_prime(31))