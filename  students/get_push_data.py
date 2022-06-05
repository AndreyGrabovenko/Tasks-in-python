from calendar import c
from itertools import zip_longest
from unittest import result


def summa(a):
    result = ''
    for i in range(3):
        result += a[i]
    return result.replace('\n', '')+'\n'


def get_data():
    with open('name.csv', 'r') as name:
        name = name.readlines()

    with open('class.csv', 'r') as classe:
        classe = classe.readlines()

    with open('adress.csv', 'r') as adress:
        adress = adress.readlines()
    list = [summa(i)for i in zip(name, classe, adress)]
    return list


def push_data(str):
    str = str.split(';')
    with open('name.csv', 'a') as name:
        for i in range(0, 5):
            name.write(str[i]+';')
        name.write('\n')
    with open('class.csv', 'a') as classe:
        classe.write(str[0]+';')
        for i in range(5, 7):
            classe.write(str[i]+';')
        classe.write('\n')
    with open('adress.csv', 'a') as adress:
        adress.write(str[0]+';')
        for i in range(7, 12):
            adress.write(str[i]+';')
        adress.write('\n')