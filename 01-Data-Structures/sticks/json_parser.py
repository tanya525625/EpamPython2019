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
    
    for curr_pair in re.finditer(r'"\w+": "(.*?)"', curr_str):   
        curr_pair = curr_pair[0].split(':')
        keys.append(curr_pair[0].replace('"', ''))
        values.append(curr_pair[1].replace('"', ''))
    obj = dict(zip(tuple(keys), tuple(values)))
    
    return obj

json_file =  open('./files/winedata_1.json', 'r')
lines = read_file(json_file)
json_file.close()
json_parser(lines)