# Дан список чисел. Создать список, в который попадают числа,
# описываемые возрастающую последовательность.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
# Порядок элементов менять нельзя

list1 =  [1, 5, 2, 3, 4, 6, 1, 7]
list2 = []
i = 0
while i < len(list1):
    if i < 1:
        if list1[i + 1] < list1[i]:
            list2.append(list1[i + 1])
            i +=2
        else:
            list2.append(list1[i])
            i +=1
    if i + 1 < len(list1):
        if list2[-1] < list1[i+1] and list1.count(list1[i+1]) ==1:
            if list2[-1] < list1[i]:
                list2.append(list1[i])
                i +=1
            else:
                list2.append(list1[i+1])
                i += 1
        elif (list1.count(list1[i]) ==1) and list2[-1] < list1[i]:
            list2.append(list1[i])
            i += 1
        else:
            i += 1
    else:
        i += 1
print(list2)