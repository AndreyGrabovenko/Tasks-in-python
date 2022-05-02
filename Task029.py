# Найти НОК двух чисел
def main():
    num_A = input("Введите число A: ")
    num_B = input("Введите число B: ")
    bool = True
    while bool:
        try:
            A = int(num_A)
            B = int(num_B)
        except ValueError:
            print('\nВведённая вами число не соотвествует параметрам целого числа!\n')
            num_A = input("Введите число A: ")
            num_B = input("Введите число B: ")
        else:
            bool = False
    print(LCM(A,B))
def LCM(A,B):
    if A>B:
        max = A
    else:
        max = B
    while True:
        if (max % A == 0) and (max % B == 0):
            lcm = max
            break
        else:
            max+=1
    return lcm
main()