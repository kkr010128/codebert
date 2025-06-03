from fractions import gcd

from functools import reduce


n = int(input())
a_list = [int(x) for x in input().split()]

temp = 1
for a in a_list:
    temp *= a // gcd(a, temp)

mod = 10 ** 9 + 7
ans = sum([temp // a for a in a_list]) % mod
print(ans)