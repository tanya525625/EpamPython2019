# Напишите реализацию функции atom, которая инкапсулирует некую переменную,
# предоставляя интерфейс для получения и изменения ее значения,
# таким образом, что это значение нельзя было бы получить или изменить
# иными способами.
# Пусть функция atom принимает один аргумент, инициализирующий хранимое значение
# (значение по умолчанию, в случае вызова atom без аргумента - None),
# а возвращает 3 функции - get_value, set_value, process_value, delete_value,такие, что:

# get_value - позволяет получить значение хранимой переменной;
# set_value - позволяет установить новое значение хранимой переменной,
# 	возвращает его;
# process_value - принимает в качестве аргументов сколько угодно функций
# 	и последовательно (в порядке перечисления аргументов) применяет эти функции
# 	к хранимой переменной, обновляя ее значение (перезаписывая получившийся
# 	результат) и возвращая получишееся итоговое значение.
# delete_value - удаляет значение

def atom(var = None):
    def get_value():
        return var

    def set_value(new_val):
        nonlocal var 
        var = new_val
        return var

    def process_value(*args):
        nonlocal var 
        for func in args:
            var = func(var)    
        return var

    def delete_value():
        nonlocal var
        del(var)
    
    return get_value, set_value, process_value, delete_value

#functions for checking
def func1(var):
    return var**3

def func2(var):
    return var + (var**2)

var = 7
new_val = 10
getter, setter, processer, deleter = atom(var)
print(setter(new_val))
print(processer(func1, func2))