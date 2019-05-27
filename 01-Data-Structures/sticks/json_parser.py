import numpy as np
import re

def read_file(file_name):
    return file_name.readlines()

def json_parser(json_file):
    obj = []
    
    json_file = str(json_file)[2:len(json_file)-2]
    json_file = json_file.replace('[', '')
    json_file = json_file.replace(']', '') 
    json_file = str(json_file).split('}, {')
    for i in range(len(json_file)):
        json_file[i] = str(json_file[i]).replace('{', '')
        obj.append(get_dict(json_file[i]))
    
    return obj
    
def get_dict(curr_str):
    keys = []
    values = []
    for curr_pair in re.finditer(r'"\w+": \w+', curr_str):
        curr_pair = curr_pair[0].split(': ')
        keys.append(curr_pair[0].replace('"', ''))
        values.append(curr_pair[1].replace('"', ''))

    for curr_pair in re.finditer(r'"\w+": "(.*?)"', curr_str):
        curr_pair = curr_pair[0].split(': ')
        keys.append(curr_pair[0].replace('"', ''))
        values.append(curr_pair[1].replace('"', '').replace("\\\\", "\\"))
    obj = dict(zip(tuple(keys), tuple(values)))
    
    for key in obj.keys():
        if obj[key] == 'null':
            obj[key] = None

    return obj

def merge_files(f1, f2):
    res = f1

    for curr_obj in f2:
        if curr_obj not in f1:
            res.append(curr_obj)

    res = sorted(res, key = lambda x: x['variety']if x['variety'] is not None else 'z')
    res = sorted(res, key = lambda x: int(x['price']) if x['price'] is not None else 0)
    res.reverse()

    return res

def write_json(obj):
    output_file =  open('./files/winedata_full.json', 'w', encoding="utf-8")

    curr_obj_ind = 0
    if len(obj) > 1:
        output_file.write('[\n')
    for i in range(len(obj)):
        curr_key_ind  = 0
        output_file.write('\t{\n')
        for key in obj[i].keys():
            if obj[i][key] == None:
                output_file.write(f'\t\t"{key}": null')
            else:
                #[1:]
                value = str(obj[i][key]).replace("\\\\", "\\")
                output_file.write(f'\t\t"{key}": "{value}"')
            if curr_key_ind != (len(obj[i].keys()) - 1):
                output_file.write(',')
            curr_key_ind += 1
            output_file.write('\n')
        if curr_obj_ind != len(obj) - 1:
            output_file.write('\t},\n')
        else:
            output_file.write('\t}\n')
        curr_obj_ind += 1
    output_file.write('\n]')
            
    output_file.close()
    

def find_options(obj):
    output_file =  open('./files/markdown_file.txt', 'w', encoding="utf-8")
    investigated_wines_list = ['Gewucrztraminer', 'Riesling', 'Merlot', 
                          'Madeira Blend', 'Tempranillo', 'Red Blend']
    investigated_obj = {
        'Gewucrztraminer': [],
        'Riesling': [],
        'Merlot': [],
        'Madeira Blend': [],
        'Tempranillo': [],
        'Red Blend': []
    }


    # options['avg_price', 'min_price', 'max_price', 'most_active_commentator', 'com_reg']
    # wine_options = dict.fromkeys(investigated_wines_list)
    # for i in range(len(obj)):
    #     output_file.write(str(obj[i]['variety']))
    #investigated_wines = []    
    price = []
    region = []
    country = []
    points = []    
    taster_name = []
    most_exp_wine = [] 
    cheap_wine = []        
    highest_score = []    
    lowest_score = []
    most_expensive_coutry = []
    cheapest_coutry = []
    most_rated_country = []
    underrated_country = []
    most_active_commentator = []

    countries = {}
    opt = {
        'prices': [],
        'scores': []
    }

    for j in range(len(investigated_wines_list)):
        for i in range(len(obj)):
            if obj[i]['variety'] == investigated_wines_list[j]:
                investigated_obj[investigated_wines_list[j]].append(obj[i])
    
    for wine in investigated_obj.keys():
        price.clear()
        region.clear()
        country.clear()
        points.clear()
        taster_name.clear()
        most_exp_wine.clear()
        cheap_wine.clear()
        highest_score.clear()
        lowest_score.clear()
        most_expensive_coutry.clear()
        cheapest_coutry.clear()
        most_rated_country.clear()
        underrated_country.clear()
        most_active_commentator.clear()

        for i in range(len(investigated_obj[wine])):
            curr_wine = investigated_obj[wine][i]
            if curr_wine['country'] != None:
                countries.update(curr_wine['country']: opt)
            if curr_wine['price'] != None:
                price.append(int(curr_wine['price']))
                countries[curr_wine['country']]['prices'].append(curr_wine['price'])
            if curr_wine['points'] != None:
                points.append(int(curr_wine['points']))
                countries[curr_wine['country']]['scores'].append(curr_wine['points'])
            if curr_wine['region_1'] != None:
                region.append(curr_wine['region_1'])
            if curr_wine['region_2'] != None:
                region.append(curr_wine['region_2'])
            if curr_wine['country'] != None:
                country.append(curr_wine['country'])
            if curr_wine['taster_name'] != None:
                taster_name.append(curr_wine['taster_name'])
            

        avg_price = np.mean(price)
        max_price = np.amax(price)
        min_price = np.amin(price)
        com_reg = max(set(region), key=region.count)
        com_country = max(set(country), key=country.count)
        avg_score = np.mean(points)
        max_score = np.amax(points)
        min_score = np.amin(points)
        act_com = max(set(taster_name), key=taster_name.count)

        output_file.write(f'{wine}\n')
        output_file.write(f'Average price is {avg_price}\n')
        output_file.write(f'Max price is {max_price}\n')
        output_file.write(f'Min price is {min_price}\n')
        output_file.write(f'Most common region is {com_reg}\n')
        output_file.write(f'Most common country is {com_country}\n')
        output_file.write(f'Average score is {avg_score}\n')
        output_file.write('=' * 20 + '\n')

        for i in price:
            if i == max_price:
                most_exp_wine.append(curr_wine['title'])
            if i == min_price:
                cheap_wine.append(curr_wine['title'])
        for i in points:
            if i == max_score:
                most_exp_wine.append(curr_wine['title'])
            if i == min_score:
                cheap_wine.append(curr_wine['title'])
        for i in taster_name:
            if i == act_com:
                most_active_commentator.append(curr_wine['taster_name'])
        for i in countries:
            if

    #print(np.mean(price))
    output_file.close()

json_file =  open('./files/winedata_1.json', 'r', encoding="utf-8")
file1 = read_file(json_file)
json_file.close()
json_file =  open('./files/winedata_2.json', 'r', encoding="utf-8")
file2 = read_file(json_file)
json_file.close()

winedata_1 = json_parser(file1)
winedata_2 = json_parser(file2)

full_winedata = merge_files(winedata_1, winedata_2)

#write_json(full_winedata)

find_options(full_winedata)
