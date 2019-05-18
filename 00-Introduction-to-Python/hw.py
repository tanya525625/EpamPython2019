# -*- coding: utf-8 -*-

"""
Реализуйте метод, определяющий, является ли одна строка 
перестановкой другой. Под перестановкой понимаем любое 
изменение порядка символов. Регистр учитывается, пробелы 
являются существенными.
"""

def is_permutation(a: str, b: str) -> bool:
    # Нужно проверить, являются ли строчки 'a' и 'b' перестановками
    if len(a) != len(b):
        return False
    else:
        dict_a = dict.fromkeys(a, 0)
        dict_b = dict.fromkeys(b, 0)

        for i in a:
            if i in dict.keys(dict_b):
                dict_a[i] += 1
            else:
                return False
        for i in b:
            if i in dict.keys(dict_a):
                dict_b[i] += 1
            else:
                return False
        
        for i in a:
            if dict_a[i] != dict_b[i]:
                return False
        
    return True

assert is_permutation('baba', 'abab')
assert is_permutation('abbba', 'abab')
