def is_armstrong(number):
    return number == sum(map(lambda x: int(x) ** len(str(number)), list(str(number))))
  
assert is_armstrong(153) == True, 'Число Армстронга'
assert is_armstrong(10) == False, 'Не число Армстронга'