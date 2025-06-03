from sys import exit
from math import gcd
n, m  = map(int, input().split())
A = list(map(int, input().split()))
Count = [0] * n

div_A = [a // 2 for a in A]

def lcm(x, y):
    return (x * y) // gcd(x, y)

for i, a in enumerate(div_A):
    while a % 2 == 0:
        Count[i] += 1
        a //= 2
if len(set(Count)) != 1:
    print(0)
    exit()

lcm_num = 1
for div_a in div_A:
    lcm_num = lcm(div_a, lcm_num)
    if lcm_num > m:
        print(0)
        exit()
else:
    print((m + lcm_num) // (2 * lcm_num))

