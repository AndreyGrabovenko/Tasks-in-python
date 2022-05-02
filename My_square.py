class my_square:
    def square_root(n):
        x = str(n)
        num, result, temp, num1 = list(x), [], [], []
        index0, index1, length1, length2, length_after_dot, count = 0, 1, 2, 0, 0, 0
        x1, y1, y2, y3 = 0, 0, 0, 0
        string_result1, string_result2 = '', ''
        exit_point = True
        try:
            point_index = num.index('.')
            for i in range(point_index):
                num1.append(num[i])
            del num[point_index]
        except ValueError:
            if len(num) % 2 == 0:
                x1 = int(num[index0] + num[index1])
                index0 += 2
                index1 += 2
            else:
                x1 = int(num[index0])
                index0 += 1
                index1 += 1
            for l in range(9, -1, -1):
                if x1 >= l*l:
                    y1 = l*2
                    result.append(l)
                    temp.append(l)
                    y3 = l*l
                    y2 = x1-y3
                    if y2 == 0 and (len(num) - (index1-2) == 0) and (len(num) == 1 or 4 or 9):
                        for i in range(len(result)):
                            string_result2 += str(result[i])
                        return float(string_result2)
                    break
            while True:
                if len(num) - length1 <= 0:
                    try:
                        length_after_dot = result.index('.')
                    except ValueError:
                        result.append('.')
                    x1 = int(str(y2) + '0' + '0')
                    y1, y2, result, temp = square_root1(y1, x1, result, temp)
                    if y2 == 0 or ((length_after_dot + 15) <= len(result)):
                        for i in range(len(result)):
                            string_result2 += str(result[i])
                        return float(string_result2)
                else:
                    x1 = int(str(y2) + num[index0] + num[index1])
                    index0 += 2
                    index1 += 2
                    length1 += 2
                    y1, y2, result, temp = square_root1(y1, x1, result, temp)
                    if y2 == 0 and (len(num) - (index1-2) == 0) and (len(num) == 1 or 4 or 9):
                        for i in range(len(result)):
                            string_result2 += str(result[i])
                        return float(string_result2)
        else:
            len_num1 = len(num1)
            len_num2 = len(num1)
            if len(num1) % 2 == 0 and len(num1) < 4: len_num2 -=1
            elif len(num1) == 1: len_num2 -=1
            while True:
                if len(num1) - length2 > 0:
                    if len_num1 % 2 == 0:
                        x1 = int(str(y2) + num1[index0] + num1[index1])
                        index0 += 2
                        index1 += 2
                        length2 += 2
                    elif exit_point:
                        x1 = int(num1[index0])
                        index0 += 1
                        index1 += 1
                        length2 += 1
                        exit_point = False
                        len_num1 += 1
                    for i in range(9, -1, -1):
                        if i*i <= x1 and count == 0:
                            count += 1
                            result.append(i)
                            temp.append(i)
                            y3 = i*i
                            for j in result: string_result1 += str(j)
                            y1 = int(string_result1) * 2
                            string_result1 = ''
                            y2 = x1-y3
                            if y2 == 0 and (len(num) - (index1-2) == 0) and (len(num) == 1 or 4 or 9):
                                for i in range(len(result)):
                                    string_result2 += str(result[i])
                                return float(string_result2)
                            if len_num1 % 2 == 0 and len(num1) > index1:
                                x1 = int(str(y2) + num1[index0] + num1[index1])
                                index0 += 2
                                index1 += 2
                                length2 += 2
                            break
                    if len_num2 >= index1-1:
                        y1, y2, result, temp = square_root1(y1, x1, result, temp)
                    if y2 == 0 and (len(num) - (index1-2) == 0) and (len(num) == 1 or 4 or 9):
                        for i in range(len(result)):
                            string_result2 += str(result[i])
                        return float(string_result2)
                else:
                    num1.clear()
                    num2 = []
                    num2.append(num[point_index:])
                    num1 = [l for x in num2 for l in x]
                    len_num1 = len(num1)
                    while True:
                        try:
                            length_after_dot = result.index('.')
                        except ValueError:
                            result.append('.')
                            length_after_dot = result.index('.')
                        if len(num) < index1:
                            x1 = int(str(y2) + '0' + '0')
                        else:
                            if len_num1 >= 2 and len(num) > index1:
                                x1 = int(str(y2) + num[index0] + num[index1])
                                index0 += 2
                                index1 += 2
                                length2 += 2
                            else:
                                x1 = int(str(y2) + num[index0] + '0')
                                index0 += 1
                                index1 += 1
                                length2 += 1
                                len_num1 += 1
                        y1, y2, result, temp = square_root1(y1, x1, result, temp)
                        if y2 == 0 or ((length_after_dot + 16) <= len(result)):
                            for i in range(len(result)):
                                string_result2 += str(result[i])
                            return float(string_result2)

def square_root1(y1, x1, result, temp):
    string_result1 = ''
    for i in range(9, -1, -1):
        if int(str(y1) + str(i)) * i <= x1:
            y4 = int(str(y1) + str(i)) * i
            result.append(i)
            temp.append(i)
            for j in temp:
                string_result1 += str(j)
            y1 = int(string_result1)*2
            y2 = x1 - y4
            break
    return y1, y2, result, temp