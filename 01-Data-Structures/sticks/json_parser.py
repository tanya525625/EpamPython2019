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

def write_json(output_file, obj):
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
            
    

def find_options(obj):
    output_file =  open('./files/markdown_file.txt', 'w', encoding="utf-8")
    output_file_stats =  open('./files/stats.json', 'w', encoding="utf-8")
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

    statistics = {
        'wine': {},
        'most_expensive_wine': [],
        'cheapest_wine': [],
        'highest_score':  [],
        'lowest_score': [],
        'most_active_commentator': []
        }

    # opt = {
    #     'prices': [],
    #     'points': [],
    #     'regions': [],
    #     'countries': [],
    #     'taster_names': [], 
    #     'average_price': 0,
    #     'min_price': 0,
    #     'max_price': 0,
    #     'max_score': 0,
    #     'min_score': 0,
    #     'most_common_region': None,
    #     'most_common_country': None,
    #     'average_score':  0,
    #     'act_com': None
    # }

    statics_for_wine = {
        'Gewucrztraminer': {
            'average_price': 0,
            'min_price': 0,
            'max_price': 0,
            'max_score': 0,
            'min_score': 0,
            'most_common_region': None,
            'most_common_country': None,
            'average_score': 0
        },
        'Riesling': {
            'average_price': 0,
            'min_price': 0,
            'max_price': 0,
            'max_score': 0,
            'min_score': 0,
            'most_common_region': None,
            'most_common_country': None,
            'average_score': 0
        },
        'Merlot': {
            'average_price': 0,
            'min_price': 0,
            'max_price': 0,
            'max_score': 0,
            'min_score': 0,
            'most_common_region': None,
            'most_common_country': None,
            'average_score': 0
        },
        'Madeira Blend': {
            'average_price': 0,
            'min_price': 0,
            'max_price': 0,
            'max_score': 0,
            'min_score': 0,
            'most_common_region': None,
            'most_common_country': None,
            'average_score': 0
        },
        'Tempranillo': {
            'average_price': 0,
            'min_price': 0,
            'max_price': 0,
            'max_score': 0,
            'min_score': 0,
            'most_common_region': None,
            'most_common_country': None,
            'average_score': 0
        },
        'Red Blend': {
            'average_price': 0,
            'min_price': 0,
            'max_price': 0,
            'max_score': 0,
            'min_score': 0,
            'most_common_region': None,
            'most_common_country': None,
            'average_score':  0
        }
    }

    most_exp_wine = []
    cheap_wine = []
    highest_score = []
    lowest_score = []
    
    # statics_for_wine = dict.fromkeys(investigated_wines_list)
    # for i in statics_for_wine.keys():
    #     statics_for_wine[i] = opt

    countries = []
    prices = []
    points = []
    commentators = []
    for j in range(len(investigated_wines_list)):
        for i in range(len(obj)):
            if obj[i]['variety'] == investigated_wines_list[j]:
                investigated_obj[investigated_wines_list[j]].append(obj[i])
                if obj[i]['country'] != None and obj[i]['country'] not in countries:
                    countries.append(obj[i]['country'])
                if obj[i]['price'] != None:
                    prices.append(int(obj[i]['price']))
                if obj[i]['points'] != None:
                    points.append(int(obj[i]['points']))
                if obj[i]['taster_name'] != None:
                    commentators.append(obj[i]['taster_name'])
    
    statistics['wine'] = statics_for_wine
    
    max_price = np.amax(prices)
    min_price = np.amin(prices)
    max_point = np.amax(points)
    min_point = np.amin(points)

    regions = []   
    countries_list = []
    
    most_com = max(set(commentators), key=commentators.count)
    statistics['most_active_commentator'] = most_com
    for wine in investigated_obj.keys():
        prices.clear()
        regions.clear()
        points.clear()
        countries_list.clear()
        wines = statistics['wine'][wine]
        for i in range(len(investigated_obj[wine])):
            curr_wine = investigated_obj[wine][i]
            
            if curr_wine['price'] != None:
                prices.append(int(curr_wine['price']))
                if int(curr_wine['price']) == max_price and curr_wine['title'] not in most_exp_wine:
                    most_exp_wine.append(curr_wine['title'])
                if int(curr_wine['price']) == min_price and curr_wine['title'] not in cheap_wine:
                    cheap_wine.append(curr_wine['title'])
                
                
            if curr_wine['points'] != None:
                points.append(int(curr_wine['points']))
                if int(curr_wine['points']) == max_point and curr_wine['title'] not in highest_score:
                    highest_score.append(curr_wine['title'])
                if int(curr_wine['points']) == min_point and curr_wine['title'] not in lowest_score:
                    lowest_score.append(curr_wine['title'])
                
            if curr_wine['region_1'] != None:
                regions.append(curr_wine['region_1'])
            if curr_wine['region_2'] != None:
                regions.append(curr_wine['region_2'])
            if curr_wine['country'] != None:
                countries_list.append(curr_wine['country'])

        wines['average_price'] = np.mean(prices)
        wines['max_price'] = np.amax(prices)
        wines['min_price'] = np.amin(prices)
        wines['most_common_region'] = max(set(regions), key=regions.count)
        wines['most_common_country'] = max(set(countries_list), key=countries_list.count)
        wines['average_score'] = np.mean(points)
        wines['max_score'] = np.amax(points)
        wines['min_score'] = np.amin(points)

        var_avg_price = wines['average_price']
        var_max_price = wines['max_price']
        var_min_price = wines['min_price']
        var_com_reg = wines['most_common_region']
        var_com_country = wines['most_common_country']
        var_avg_score = wines['average_score']

        output_file.write(f'{wine}\n')
        output_file.write(f'Average price is {var_avg_price}\n')
        output_file.write(f'Max price is {var_max_price}\n')
        output_file.write(f'Min price is {var_min_price}\n')
        output_file.write(f'Most common region is {var_com_reg}\n')
        output_file.write(f'Most common country is {var_com_country}\n')
        output_file.write(f'Average score is {var_avg_score}\n')
        output_file.write('=' * 30 + '\n')
        
    statistics['most_expensive_wine'] = most_exp_wine
    statistics['cheapest_wine'] = cheap_wine
    statistics['highest_score'] = highest_score
    statistics['lowest_score'] = lowest_score
    
    output_file.write(f'The most expensive wine is {max_price}. They are {most_exp_wine}\n')
    output_file.write('=' * 30 + '\n')
    output_file.write(f'The cheapest wine is {min_price}. They are {cheap_wine}\n')
    output_file.write('=' * 30 + '\n')
    output_file.write(f'The highest score is {max_point}. They are {highest_score}\n')
    output_file.write('=' * 30 + '\n')
    output_file.write(f'The highest score is {min_point}. They are {lowest_score}\n')
    output_file.write('=' * 30 + '\n')
    output_file.write(f'The most active commentator is {most_com}\n')
    output_file.write('=' * 30 + '\n')

    countries_info = dict.fromkeys(tuple(countries))
    for key in countries_info.keys():
        countries_info[key] = {}

    high_avg_price = 0
    low_avg_price = None
    high_avg_score = 0
    low_avg_score = None

    country_prices = []
    country_points = []
    for country in countries_info.keys():
        country_prices.clear()
        country_points.clear()
        for wine in investigated_obj.keys():
            for i in range(len(investigated_obj[wine])):
                curr_wine = investigated_obj[wine][i]
                if curr_wine['country'] == country:
                    if curr_wine['price'] != None:
                        country_prices.append(int(curr_wine['price']))
                    if curr_wine['points'] != None:
                        country_points.append(int(curr_wine['points']))
        avg_price = np.mean(country_prices)
        avg_score = np.mean(country_points)
        if low_avg_price == None:
            low_avg_price = avg_price
            statistics['cheapest_coutry'] = [country, low_avg_price]
        if low_avg_score == None:
            low_avg_score = avg_score
            statistics['underrated_country'] = [country, low_avg_score]
        if avg_price > high_avg_price:
            high_avg_price = avg_price
            statistics['most_expensive_country'] = [country, avg_price]
        if avg_price < low_avg_price:
            low_avg_price = avg_price
            statistics['cheapest_coutry'] = [country, avg_price]
        if avg_score > high_avg_score:
            high_avg_score = avg_score
            statistics['most_rated_country'] = [country, avg_score]
        if avg_price < low_avg_score:
            low_avg_score = avg_score
            statistics['underrated_country'] = [country, avg_score]

    output_file.close()

    output_file_stats =  open('./files/stats.json', 'w', encoding="utf-8")
    output_file_stats.write('{"statistics": {\n')
    
    ind = 0
    for key in statistics.keys():
        output_file_stats.write('\t\"' + key + '": ')
        if key == 'wine': 
            output_file_stats.write("{\t\n")
            ind_key_wine = 0
            for key_wine in statistics[key].keys():
                output_file_stats.write('\t\t\"' + key_wine + '": {\n')
                i = 0
                for key_var in statistics[key][key_wine].keys():
                    output_file_stats.write('\t\t\t\"' + key_var + '":"' 
                                            +  str(statistics[key][key_wine][key_var]) + '"')
                    if i < len(statistics[key][key_wine]) - 1:
                        output_file_stats.write(",")
                    else:
                        output_file_stats.write("\n\t\t\t}")
                        if ind_key_wine < len(statistics[key]) - 1:
                            output_file_stats.write(",")
                    output_file_stats.write("\n")   
                    i += 1
                ind_key_wine += 1 
            output_file_stats.write("\n}")  
        else:
            #print(ind)
            # if ind == 1:
            #     output_file_stats.write("\n}")  
            val = str(statistics[key]).replace("\\'", '').replace("'", '"').replace("\\", '')
            if key == 'most_active_commentator': 
                output_file_stats.write(f'"{val}"')
            else:
                output_file_stats.write(val)    
        #output_file_stats.write("\n") 
            
        if ind < len(statistics) -  1 :
            output_file_stats.write(",\n")
        ind += 1 
    output_file_stats.write('\n\t}')
    output_file_stats.write('\n}')
    output_file_stats.close()
    return statistics

json_file =  open('./files/winedata_1.json', 'r', encoding="utf-8")
file1 = read_file(json_file)
json_file.close()
json_file =  open('./files/winedata_2.json', 'r', encoding="utf-8")
file2 = read_file(json_file)
json_file.close()

winedata_1 = json_parser(file1)
winedata_2 = json_parser(file2)

full_winedata = merge_files(winedata_1, winedata_2)

output_file_winedata =  open('./files/winedata_full.json', 'w', encoding="utf-8")
#write_json(output_file_winedata, full_winedata)
output_file_winedata.close()

statistics = find_options(full_winedata)
