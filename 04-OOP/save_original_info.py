# Переписать функцию make_cache, которая сохраняет
# результаты предыдущих вызовов оборачиваемой функции,
# таким образом, чтобы она сохраняла результаты в своем
# хранилищe на определенное время, которое передается
# параметром (аргументом) в декоратор.

# Плюс придумать некоторый полезный юзкейс 
# и заимплементировать функцию slow_function
import time


def make_cache(bound):
    def modify_func(func):
        def new_function(*args, **kwargs):
            cache = []
            cache.append(func(*args, **kwargs))
            for i in range(len(cache)):
                if (time.time() - cache[i]['time']) > bound:
                    cache.pop(0)
            return cache
        return new_function
    return modify_func


@make_cache(30)
def slow_function(type_of_payment, customer_name):
    """
    A func for storaging information about purchase
    in the shop. If the warranty expires, the information
    will be deleted.
    """
    product = {
        'type_of_payment': type_of_payment,
        'customer': customer_name, 
        'time': time.time()
        }
    return product

print(slow_function('card', 'Ivanov'))