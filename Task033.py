# 33.	Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# 1.	k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
k = 2
list_of_coefficients = [int(random.randint(1,101)) for i in range(k+1)]
with open('polynomial_file.txt', 'w') as f:
    f.writelines(str(f'{list_of_coefficients[2]} * x**2 + {list_of_coefficients[1]} * x + {list_of_coefficients[0]} = 0'))

list_of_coefficients = [int(random.randint(0,101)) for i in range(k+1)]
with open('polynomial_file1.txt', 'w') as f:
    f.writelines(str(f'{list_of_coefficients[2]} * x**2 + {list_of_coefficients[1]} * x + {list_of_coefficients[0]} = 0'))