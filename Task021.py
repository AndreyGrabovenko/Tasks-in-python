# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

list1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
list2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
list3 = ["йцу", "фыв", "ячс", "цук", "йцукен"]
list4 = ["123", "234", 123, "567"]
list5 = []

search1='qwe'
search2='йцу'
search3='йцу'
search4='123'
search5='123'

def Search(search1, list):
    count, count1, a, x = 0, -1, -1, len(list)
    if x == 0: return a
    while True:
        for i in list:
            count1+=1
            if count1 == x: return a
            try:
                if search1 == i:
                    count+=1
                    if count == 2:
                        a = count1
                        return a
            except UnboundLocalError:
                return a

print('список 1 имеет позицию второго вхождения строки', Search(search1, list1))
print('список 2 имеет позицию второго вхождения строки', Search(search2, list2))
print('список 3 имеет позицию второго вхождения строки', Search(search3, list3))
print('список 4 имеет позицию второго вхождения строки', Search(search4, list4))
print('список 5 имеет позицию второго вхождения строки', Search(search5, list5))
