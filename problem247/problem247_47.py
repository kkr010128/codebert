from fractions import gcd
from functools import reduce
import sys


def lcm_base(x, y):
    return (x * y) // gcd(x, y)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

# def lcm_list(numbers, maxvalue):
#     first = 1
#     second = 1
#     for i in numbers:
#         second = i
#         lcm_result = lcm_base(first, second)
#         if lcm_result > maxvalue:
#             return -1
#         first = lcm_result
#     return lcm_result


n, m = map(int, input().split())
A = list(map(int, input().split()))

max_value = 2 * m

try:
    lcm = lcm_list(A)
except:
    print("0")
    sys.exit(0)

if lcm > max_value:
    print("0")
    sys.exit(0)

if lcm == -1:
    print("0")
    sys.exit(0)

if any((lcm / a) % 2 != 1 for a in A):
    print("0")
    sys.exit(0)

max_product = max_value // lcm
print((max_product + 1) // 2)
