def import_col_file():  # импортируем файл с записью колонкой
    with open('base_col.csv', 'r') as file:
        data = file.readlines()
    return data


def import_row_file():  # импортируем файл с записью строками
    with open('base_row.csv', 'r') as file:
        data = file.read()
    return data