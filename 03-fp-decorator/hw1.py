from functools import reduce


# problem 6
def sum_squares(bound):
    return sum(range(bound+1))**2 - sum(x**2 for x in range(bound+1))


# problem 9
def find_triplet(sum):
    return [(a, b, sum-a-b) for a in range(1, sum) for b in range(1, sum)
            if ((a**2 + b**2) == (sum-a-b)**2) and a < b]


# problem 48
def find_last_digits(bound):
    return str(sum(i**i for i in range(bound+1)))[-10:]


# problem 40
def find_mult_digits(positions):
    string = ''.join([str(i) for i in range(positions[-1])])
    return reduce(lambda x, y: int(x) * int(y), [string[i] for i in positions])

print(find_triplet(1000))
print(sum_squares(100))
print(find_last_digits(1000))
print(find_mult_digits([1, 10, 100, 1000, 10000, 100000, 1000000]))
