# Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

def main():
    week = {1:'Понедельник', 2:'Вторник', 3:'Среда',
            4:'Четверг', 5:'Пятница', 6:'Субота', 7:'Воскресенье'}
    num = input("Введите число обозначающее день недели: ")
    bool = True
    while bool:
        try:
            numbers = int(num)
            if numbers <= 7 and numbers >= 1:
                bool = False
        except ValueError:
            print('Введите правильно число!')
            num = input("Введите число от 1 до 7: ")
        except TypeError:
            print('Введите правильно число!')
            num = input("Введите число от 1 до 7: ")
        except UnboundLocalError:
            print('Введите правильно число!')
            num = input("Введите число от 1 до 7: ")
    if numbers == 6 or numbers == 7:
        print('Число', numbers, 'является выходным днём и это', week[numbers])
    else:
        print('Число', numbers, 'не является выходным днём! это будний день', week[numbers])
main()