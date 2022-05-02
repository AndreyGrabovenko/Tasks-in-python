# 34.	Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def main():
    f = open('polynomial_file.txt', 'r')
    x = f.readline()
    y = open('polynomial_file1.txt', 'r')
    l = y.readline()
    f.close()
    y.close()
    list1 = finding_coefficients(x)
    list2 = finding_coefficients(l)
    list_of_coefficients = [list1[i] + list2[i] for i in range(len(list1))]
    with open('polynomial_file2.txt', 'w') as f:
        f.writelines(str(f'{list_of_coefficients[0]} * x**2 + {list_of_coefficients[1]} * x + {list_of_coefficients[2]} = 0'))

def finding_coefficients(x):
    lists = []
    r = ''
    count = 0
    while True:
        if x[count] == '=':
            return lists
        if (x[count] + x[count+1]) == '*2':
            count += 2
        elif  x[count].isdigit():
            r += x[count]
            count+=1
        elif r.isdigit() :
            lists.append(int(r))
            count+=1
            r = ''
        else:
            count += 1

main()

