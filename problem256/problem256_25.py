import fractions
from functools import reduce
def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

A,B=list(map(int,input().split()))
print(lcm_list([A,B]))