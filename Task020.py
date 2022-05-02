# Определить, присутствует ли в заданном списке строк, некоторое число

lists = ['a', 'b', 'c', 'd', 84, 85, 'e', 'f', 9, 5]
for i in lists:
    a = str(i).isdigit()
    if a == True: print(i)