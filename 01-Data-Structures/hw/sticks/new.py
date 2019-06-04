# -*- coding: utf-8 -*-
print("""Не советую запускать! Придется ждать очень долго!!""")
dic = {}


def func(file):
    '''
    Запись во временную переменную поочередно информации
            хранящейся между {}
    '''
    # new_string = ''
    temp_string = ''
    for line in file:
        for sym in line:
            if sym in '{[':
                continue
            if sym == '\n':
                continue
            if sym != '}':
                temp_string += sym
                if temp_string == ',':
                    temp_string = ''
                elif temp_string == ' ':
                    temp_string = ''
            else:
                # print()
                # print('TEMP STRING', temp_string)
                other_func(temp_string)
                temp_string = ''
            # print(new_string)
    # print(new_string)


def other_func(string):
    '''
    Сплитит данные и записывает в словарь
    '''
    global dic
    new_string = string .split(', "')
    # print('STRING', new_string)
    for stk in range(len(new_string)):
        new_string[stk] = new_string[stk].replace('"', '')
    # print('NEW STRING', new_string)
    stroka = 0
    while stroka != (len(new_string)):
        # print("STROKA", stroka)
        new_stroka = new_string[stroka].split(': ')
        # print("NEW_STROKA", new_stroka)
        if new_stroka[0] not in dic:
            dic[new_stroka[0]] = [new_stroka[1], ]
        elif new_stroka[0] == 'title':
            temp_name = 'title'
            temp_title = new_stroka[1]
        elif new_stroka[0] == 'taster_name':
            if check_dic(temp_name, temp_title, dic, new_stroka[1]):
                dic['points'].pop()
                dic['description'].pop()
                stroka = 12
            else:
                dic[temp_name] += [temp_title, ]
                dic['taster_name'] += [new_stroka[1], ]
        else:
            dic[new_stroka[0]] += [new_stroka[1], ]
        stroka += 1


def check_dic(temp_name, temp_title, dic, new_stroka):
    '''Проверка повторяющихся данных'''
    if temp_title in dic[temp_name]:
        if new_stroka in dic['taster_name']:
            return True
    return False


def merge_files(wd, wd2):
    '''Объединение двух файлов'''
    merge_text = wd.read()[:-1]+wd2.read()[1:]
    with open('./ready_winedata.json', 'w') as rwd:
        rwd.write(merge_text)


with open('./winedata_1.json') as wd:
    with open('./winedata_2.json') as wd2:
        merge_files(wd, wd2)

with open('./ready_winedata.json', 'r') as rwd:
    print(func(rwd))
