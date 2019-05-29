# Напишите реализацию функции make_it_count, которая принимает в качестве
# аргументов некую функцию (обозначим ее func) и имя глобальной переменной
# (обозначим её counter_name), возвращая новую функцию, которая ведет себя
# в точности как функция func, за тем исключением, что всякий раз при вызове
# инкрементирует значение глобальной переменной с именем counter_name.

def func():
    print("Just a function")

def make_it_count(func, counter_name):
    def count_func():
        global counter_name
        counter_name += 1
        func()
    return count_func

counter_name = 0
count_func = make_it_count(func, counter_name)
count_func()
print(counter_name)