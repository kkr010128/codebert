from math import gcd
from itertools import combinations


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors


def is_prime(p):
    if p == 1:
        return False
    for i in range(2, int(p**.5) + 1):
        if p % i == 0:
            return False
    return True


a, b = map(int, input().split())
se = set(make_divisors(a)) & set(make_divisors(b))
ans = 1
for i in se:
    if is_prime(i):
        ans += 1
print(ans)
