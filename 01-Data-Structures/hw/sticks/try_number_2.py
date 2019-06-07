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
merged_winedatas = sorted(merged_winedatas, key=sort_by_price)
write_data_to_file(merged_winedatas)


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
            if i != '0':
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
            correct_dict[i] = int(score_dict[i][0]) / score_dict[i][1] if score_dict[i][1] > 0 \
                else 'null'
        return correct_dict


def most_expensive_wine(file):
    list_of_wines = []
    price = int(file[-1]['price'])
    list_of_wines.append(file[-1]['designation'])
    for i in file[-2::-1]:
        if int(i['price']) < price:
            break
        list_of_wines.append(i['designation'])
    list_of_wines = set(list_of_wines)
    return list_of_wines


def cheapest_wine(file):
    list_of_wines = []
    price = int(file[0]['price'])
    list_of_wines.append(file[0]['designation'])
    for i in file[1:]:
        if int(i['price']) > price:
                break
        list_of_wines.append(i['designation'])
    list_of_wines = set(list_of_wines)
    return list_of_wines


def highest_lowest_score(file):
    low_score = {}
    high_score = {}
    file = sorted(file, key=sort_by_score)
    lw_score = int(file[0]['points'])
    hg_score = int(file[-1]['points'])
    low_score[file[0]['designation']] = int(file[0]['points'])
    high_score[file[-1]['designation']] = int(file[-1]['points'])
    for i in file[1:]:
        if int(i['points']) > lw_score:
            break
        if i['designation'] not in low_score:
            low_score[i['designation']] = int(i['points'])
    for j in file[-2::-1]:
        if int(j['points']) < hg_score:
            break
        if j['designation'] not in high_score:
            high_score[j['designation']] = int(j['points'])
    return high_score, low_score


def sort_by_score(wd):
    return wd['points']


def most_rated_underrated_country(file):
    dict_of_country = {}
    for i in file:
        if i['country'] not in dict_of_country:
            dict_of_country[i['country']] = 1
        else:
            dict_of_country[i['country']] += 1
    rated = 0
    rt_country = ''
    undr_country = ''
    for i in dict_of_country:
        if dict_of_country[i] > rated:
            rated = dict_of_country[i]
            rt_country = i
    for j in dict_of_country:
        if dict_of_country[j] < rated:
            rated = dict_of_country[j]
            undr_country = j
    return rt_country, undr_country


def most_active_commentator(file):
    commentators = {}
    for i in file:
        if i['taster_twitter_handle'] not in commentators:
            commentators[i['taster_twitter_handle']] = 1
        else:
            commentators[i['taster_twitter_handle']] += 1
    maxi = 0
    comment = ''
    for i in commentators:
        if commentators[i] > maxi:
            comment, maxi = i, commentators[i]
    return comment


varieties = ["Gew\\u00fcrztraminer", "Riesling", "Merlot", "Madera", "Tempranillo", "Red Blend"]
price = avarege_price(merged_winedatas, varieties)
print(price)
mx_mn_price = max_min_price(merged_winedatas, varieties)
print(mx_mn_price)
reg_country = most_common_region_country(merged_winedatas, varieties)
print(reg_country)
avar_score = avarege_score(merged_winedatas, varieties)
print(avar_score)
most_expens = most_expensive_wine(merged_winedatas)
print(most_expens)
cheap_w = cheapest_wine(merged_winedatas)
h_l_score = highest_lowest_score(merged_winedatas)
r_undr_count = most_rated_underrated_country(merged_winedatas)
comment = most_active_commentator(merged_winedatas)

need_to_find = ['avarege_price', 'min_price', 'max_price', 'most_common_region', 'most_common_country', 'avarege_score']
need_find = [avarege_price, max_min_price, most_common_region_country, avarege_score]
dict_of_found = {"statistics": {
                        "wine": {
                            "Gew\\u00fcrztraminer": {"avarege_price": price["Gew\\u00fcrztraminer"],
                                                     "min_price": mx_mn_price["Gew\\u00fcrztraminer"][1],
                                                     "max_price": mx_mn_price["Gew\\u00fcrztraminer"][0],
                                                     "most_commot_region": reg_country[0]["Gew\\u00fcrztraminer"],
                                                     "most_common_country": reg_country[1]["Gew\\u00fcrztraminer"],
                                                     "avarege_score": avar_score["Gew\\u00fcrztraminer"]},
                            "Riesling": {"avarege_price": price["Riesling"],
                                         "min_price": mx_mn_price["Riesling"][1],
                                         "max_price": mx_mn_price["Riesling"][0],
                                         "most_commot_region": reg_country[0]["Riesling"],
                                         "most_common_country": reg_country[1]["Riesling"],
                                         "avarege_score": avar_score["Riesling"]},
                            "Merlot": {"avarege_price": price["Merlot"],
                                       "min_price": mx_mn_price["Merlot"][1],
                                       "max_price": mx_mn_price["Merlot"][0],
                                       "most_commot_region": reg_country[0]["Merlot"],
                                       "most_common_country": reg_country[1]["Merlot"],
                                       "avarege_score": avar_score["Merlot"]},
                            "Madera": {"avarege_price": price["Madera"],
                                       "min_price": mx_mn_price["Madera"][1],
                                       "max_price": mx_mn_price["Madera"][0],
                                       "most_commot_region": reg_country[0]["Madera"],
                                       "most_common_country": reg_country[1]["Madera"],
                                       "avarege_score": avar_score["Madera"]},
                            "Tempranillo": {"avarege_price": price["Tempranillo"],
                                            "min_price": mx_mn_price["Tempranillo"][1],
                                            "max_price": mx_mn_price["Tempranillo"][0],
                                            "most_commot_region": reg_country[0]["Tempranillo"],
                                            "most_common_country": reg_country[1]["Tempranillo"],
                                            "avarege_score": avar_score["Tempranillo"]},
                            "Red Blend": {"avarege_price": price["Red Blend"],
                                          "min_price": mx_mn_price["Red Blend"][1],
                                          "max_price": mx_mn_price["Red Blend"][0],
                                          "most_commot_region": reg_country[0]["Red Blend"],
                                          "most_common_country": reg_country[1]["Red Blend"],
                                          "avarege_score": avar_score["Red Blend"]}},
    "most_expensive_wine": most_expens,
    "cheapest_wine": cheap_w,
    "highest_score": h_l_score[0],
    "lowest_score": h_l_score[1],
    "most_rated_country": r_undr_count[0],
    "underrated_country": r_undr_count[1],
    "most_active_commentator": comment}}

with open('stats.json', 'w') as stat:
    stat.writelines(str(dict_of_found))
