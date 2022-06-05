import import_file
import export_file
import ui

# импорт из файлов с разными формами записи с переводом в одинаковый двумерный массив


def download_guide(a):
    if a == 'col':
        in_list = import_file.import_col_file()
        in_list1 = [i.replace('\n', '') for i in in_list]
        in_list1 = list(filter(None, in_list1))
        in_list2 = [in_list1[i:i+4] for i in range(0, len(in_list1), 4)]
    if a == 'row':
        in_list = import_file.import_row_file().strip().replace(
            '"', '').replace(' ', '').split('\n')
        in_list2 = [i.split(';') for i in in_list]
    print(in_list2, '\nОтлично, загрузили справочник! ')
    return in_list2


def upload_guide(a, massive):  # выгрузка в файл
    if a == 'col':
        export_file. export_col(massive)
    if a == 'row':
        export_file. export_row(massive)
    print('\nВсё хорошо справочник выгружен! ')


def run():
    temp = ui.initial()
    guide = download_guide(temp)
    temp = ui.next_operation()
    while temp[0] != 4:

        if temp[0] == 1 and temp[1] == 'col':
            download_guide('col')
            temp = ui.next_operation()

        if temp[0] == 1 and temp[1] == 'row':
            download_guide('row')
            temp = ui.next_operation()

        if temp[0] == 2 and temp[1] == 'col':
            upload_guide('col', guide)
            temp = ui.next_operation()

        if temp[0] == 2 and temp[1] == 'row':
            upload_guide('row', guide)
            temp = ui.next_operation()
        if temp[0] == 3:
            print(ui.added_abonent(guide))
            temp = ui.next_operation()