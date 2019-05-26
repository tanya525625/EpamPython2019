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
        curr_pair = curr_pair[0].split(':')
        keys.append(curr_pair[0].replace('"', ''))
        values.append(curr_pair[1].replace('"', ''))

    for curr_pair in re.finditer(r'"\w+": "(.*?)"', curr_str):
        curr_pair = curr_pair[0].split(':')
        keys.append(curr_pair[0].replace('"', ''))
        values.append(curr_pair[1].replace('"', ''))
    obj = dict(zip(tuple(keys), tuple(values)))
    
    for key in obj.keys():
        if obj[key] == ' null':
            obj[key] = None

    return obj

def merge_files(f1, f2):
    res = f1

    for curr_obj in f2:
        if curr_obj not in f1:
            res.append(curr_obj)

    res = sorted(res, key = lambda x: x['title'])
    res = sorted(res, key = lambda x: int(x['price']) if x['price'] is not None else 0)
    res.reverse()

    return res

def save_json(obj):
    output_file =  open('./files/winedata_full.json', 'w')
    str_obj = str(obj).replace("' ",'"')
    str_obj = str(obj).replace("'",'"')
    #print(str_obj)
    count = 0
    count = 0
    quotes_count = 0

    for curr_char in str_obj:
        if curr_char == '[' or curr_char == ']' or curr_char == '{' or curr_char == '}':
            if curr_char == '[':
                if count > 0:
                    for i in range(count):
                        output_file.write('\t')
                output_file.write(f'{curr_char}\n')
                count += 1
            if curr_char == ']':
                count -= 1
                output_file.write(f'\n{curr_char}')
            if curr_char == '{':
                if count > 0:
                    for i in range(count):
                        output_file.write('\t')
                count += 1
                output_file.write(f'{curr_char}\n')
            if curr_char == '}':
                count += 1
                output_file.write(f'\n{curr_char}')
        else:
            if curr_char == '"':
                if quotes_count == 0:
                    output_file.write('\t')
                quotes_count += 1
            elif curr_char == ',' and quotes_count % 2 == 0:
                output_file.write(',\n')
            else:
                output_file.write(curr_char)
            
    output_file.close()
    

json_file =  open('./files/winedata_1.json', 'r')
file1 = read_file(json_file)
json_file.close()
json_file =  open('./files/winedata_2.json', 'r')
file2 = read_file(json_file)
json_file.close()

winedata_1 = json_parser(file1)
winedata_2 = json_parser(file2)

full_winedata = merge_files(winedata_1, winedata_2)

save_json(full_winedata)
