# Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел

def main():
    num = input("Введите строку чисел разделёную пробелом: ")
    bool = True
    while bool:
        try:
            a = []
            for i in num.split(' '):
                    a.append(float(i))
        except ValueError:
            print('\nВведённая вами строка не соотвествует параметрам!\n')
            num = input("Введите строку чисел разделёную пробелом: ")
        else:
            bool = False
    print('\n',a,'\n')
    print('max =', max(a))
    print('min =', min(a),'\n')
main()