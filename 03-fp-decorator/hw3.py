# Гипотеза может быть кратко выражена следующим образом:

# берём любое натуральное число n, если оно чётное, то делим его на 2
# если нечётное, то умножаем на 3 и прибавляем 1 (получаем 3n + 1)
# над полученным числом выполняем те же самые действия, и так далее
# Гипотеза Коллатца заключается в том, что какое бы начальное число n мы ни взяли, рано или поздно мы получим единицу.

def collatz_steps(n, k = 0):
    return collatz_steps(n/2 if n % 2 == 0 else 3*n + 1, k = k + 1) if n > 1 else k
 
assert collatz_steps(16) == 4
assert collatz_steps(12) == 9
assert collatz_steps(1000000) == 152