# Find the sum of all the multiples of 3 or 5 below 1000.
def find_sum(bound):
    return sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(bound)))

# Find the difference between the sum of the squares of the first 
# one hundred natural numbers and the square of the sum.
def sum_squares(bound):
    return sum(range(bound+1))**2 - sum(x**2 for x in range(bound+1))

#Find the sum of all the numbers that can be written 
# as the sum of fifth powers of their digits.
def sum_of_fifth_pow_of_numb(bound):
    return sum(s for s in range(bound) if s == sum(int(x)**5 
                                 for x in list(str(s)))) - 1    

print(find_sum(1000))
print(sum_of_fifth_pow_of_numb(500000))
print(sum_squares(100))