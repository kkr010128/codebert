from fractions import gcd

from functools import reduce


n = int(input())
a_list = [int(x) for x in input().split()]

temp = reduce(lambda x, y: (x * y) // gcd(x, y), a_list)

mod = 10 ** 9 + 7
ans = sum([temp // a for a in a_list]) % mod
print(ans)