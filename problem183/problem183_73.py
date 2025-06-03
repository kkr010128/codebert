import math


def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    # divisors.sort()
    return divisors


n = int(input())

d2 = make_divisors(n - 1)
ans = len(d2)

for k in make_divisors(n):
    if k == 1:
        continue
    tmp = n
    while tmp % k == 0:
        tmp //= k

    if tmp % k == 1:
        d2.append(k)

print(len(d2) - 1)
