import csv


def export_col(list):  # экспорт в файл колонкой
    with open('output_col.csv', 'w') as file:
        for i in range(0, len(list)):
            for j in range(0, 4):
                print(list[i][j])
                file.write(f'{list[i][j]} \n')
            print()
            file.write(f'\n')


def export_row(list):  # экспорт в файл строчкой
    with open('output_row.csv', 'w') as file:
        for i in range(len(list)):
            a = ''
            for j in range(0, 4):
                a += list[i][j]+';'
            a = a[:-1]
            print(a)
            file.write(f'"{a}"\n')