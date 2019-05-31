import string

def letters_range(*args, **kwargs):
    arg_count = len(args)

    if arg_count == 0 or arg_count > 3:
         raise Exception('Wrong number of arguments')
    else:
        letters_list = [ch for ch in string.ascii_lowercase]
        if kwargs:
            for key in kwargs:
                ind = letters_list.index(key)
                letters_list[ind] = kwargs[key]

        limiters = {
            'start': 0,
            'stop': None, 
            'step': 1
        }

        if arg_count == 3 or arg_count == 2:
            for i, key in enumerate(limiters.keys()):
                if i > arg_count - 1:
                    break
                else:
                    if i == 2:  # if it is a step
                        limiters[key] = args[i]
                    else:   
                        limiters[key] = letters_list.index(args[i])
        else:
            limiters['stop'] = letters_list.index(args[0])
        
        return letters_list[limiters['start']:limiters['stop']:limiters['step']]

print(letters_range('b', 'w', 2))
print(letters_range('g'))
print(letters_range('g', 'p'))
print(letters_range('g', 'p', **{'l': 7, 'o': 0}))
print(letters_range('p', 'g', -2))
print(letters_range('a'))