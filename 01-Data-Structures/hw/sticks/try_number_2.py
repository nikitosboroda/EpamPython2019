# -*- coding: utf-8 -*-


def convert_file_to_data(file_direct):
    """Берем данные из файла и записываем в питоновские структуры данных"""
    file = open(file_direct, encoding='ascii')
    file_data = file.read()
    file.close()
    file_data = file_data.replace('[', '')
    file_data = file_data.replace(']', '')
    file_data = file_data.replace('\'', '')
    file_data = file_data.replace('null', '0')
    file_data = file_data.split('}, {')  # была строка, стал список
    list_of_dicts = []
    for i in range(0, len(file_data)):
        key_json, value_json = [], []
        if '{' in file_data[i]:
            file_data[i] = file_data[i].replace('{', '')
        if '}' in file_data[i]:
            file_data[i] = file_data[i].replace('}', '')
        temp_data = file_data[i].split(', "')  # делаем еще больше списков
        for j in range(0, len(temp_data)):
            temp_data[j] = temp_data[j].replace('"', '')
        for k in range(0, len(temp_data)):
            temp = temp_data[k]
            temp = temp.split(': ')
            key_json.append(temp[0])
            value_json.append(temp[1])
        temp_dict = {}
        for ii in range(len(key_json)):
            temp_dict[key_json[ii]] = value_json[ii]
        list_of_dicts.append(temp_dict)
    return list_of_dicts


def merge_files(wd1, wd2):
    """Объединяем все данные в одину структуру"""
    if len(wd1) > len(wd2):
        merged_file = wd1
        little = wd2
    else:
        merged_file = wd2
        little = wd1
    for i in little:
        if i not in merged_file:
            merged_file.append(i)
    return merged_file


def write_data_to_file(merged_wd):
    """Записываем данные в выходной файл"""
    ready_file = open('ready_winedata.json', 'w', encoding='ascii')
    ready_file.write(str(merged_wd[-1::-1]))  # данные отсортированы по возростанию, поэтому пишем с конца
    ready_file.close()


def sort_by_price(wd):
    return wd['price']


file1 = 'winedata_1.json'
file2 = 'winedata_2.json'

winedata1 = convert_file_to_data(file1)
winedata2 = convert_file_to_data(file2)
merged_winedatas = merge_files(winedata1, winedata2)
# merged_winedatas = sorted(merged_winedatas, key=sort_by_price)
# write_data_to_file(merged_winedatas)


# Начинается сбор данных для 3го задания


def avarege_price(file, variety):
    variety_prices_dict = {i: [0, 0] for i in variety}
    for j in file:
        # print(j)
        if j['variety'] in variety:
            # print(j['variety'])
            variety_prices_dict[j['variety']][0] += int(j['price'])
            variety_prices_dict[j['variety']][1] += 1
    correct_dict = {i: 0 for i in variety_prices_dict}
    for i in correct_dict:
        correct_dict[i] = int(variety_prices_dict[i][0])/variety_prices_dict[i][1] if variety_prices_dict[i][1] > 0 \
            else 'null'
    return correct_dict


def max_min_price(file, variety):
    price_dict_of_sorts = {i: [0, 0] for i in variety}
    for j in file:
        if j['variety'] in variety:
            if int(j['price']) > price_dict_of_sorts[j['variety']][0]:
                price_dict_of_sorts[j['variety']][0] = int(j['price'])
            elif int(j['price']) <= price_dict_of_sorts[j['variety']][0]:
                price_dict_of_sorts[j['variety']][1] = int(j['price'])
    return price_dict_of_sorts


def most_common_region_country(file, variety):
    dict_of_varity = {i: [{}, {}] for i in variety}
    # для каждого сорта(ключа) - значения -> список из словарей с подсчитанными регионами и странами
    for j in file:
        if j['variety'] in variety:
            if j['region_1'] not in dict_of_varity[j['variety']][0]:
                dict_of_varity[j['variety']][0][j['region_1']] = 1
            else:
                dict_of_varity[j['variety']][0][j['region_1']] += 1
            if j['country'] not in dict_of_varity[j['variety']][1]:
                dict_of_varity[j['variety']][1][j['country']] = 1
            else:
                dict_of_varity[j['variety']][1][j['country']] = 1
    common_region_var = {}
    common_country_var = {}
    for var in dict_of_varity:
        max_reg, max_cntry = 0, 0
        common_region, common_country = '', ''
        country = dict_of_varity[var].pop()
        region = dict_of_varity[var].pop()
        for i in region:
            if i != '0' :
                if region[i] > max_reg:
                    max_reg = region[i]
                    common_region = i
        for i in country:
            if i != '0':
                if country[i] > max_cntry:
                    max_cntry = country[i]
                    common_country = i
        common_region_var[var] = common_region
        common_country_var[var] = common_country
    return common_region_var, common_country_var


def avarege_score(file, variety):
    score_dict = {i: [0, 0] for i in variety}
    for j in file:
        if j['variety'] in variety:
            score_dict[j['variety']][0] += int(j['points'])
            score_dict[j['variety']][1] += 1
        correct_dict = {i: 0 for i in score_dict}
        for i in correct_dict:
            correct_dict[i] = int(score_dict[i][0]) / score_dict[i][1] if variety_prices_dict[i][
                                                                                                1] > 0 \
                else 'null'
        return correct_dict


def most_expensive_wine(file):
    list_of_wines = []
    price = int(file[0]['price'])
    list_of_wines.append(price)
    for i in file[1:]:
        if i['price'] < price:
            break
        list_of_wines.append(i['price'])
    return list_of_wines
            


varieties = ["Gew\\u00fcrztraminer", "Riesling", "Merlot", "Madera", "Tempranillo", "Red Blend"]
need_to_find = ["avarege_price", "min_price", "max_price", "most_common_region", "most_common_country", "avarege_score"]
dict_of_found = {"statistics": {
                        "wine": {
                                i: {} for i in varieties}}}

# price = avarege_price(merged_winedatas, varieties)
# print(price)
# price = max_min_price(merged_winedatas, varieties)
# print(price)
# region = most_common_region_country(merged_winedatas, varieties)
# print(region)
# avarege_score(merged_winedatas, varieties)

