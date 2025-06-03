import sys
import math

A, B = map(int, sys.stdin.readline().split())
gcd = math.gcd(A, B)


def factrization_prime(number):
    factor = {}
    div = 2
    s = math.sqrt(number)
    # print(s)
    while div < s:
        div_cnt = 0
        while number % div == 0:
            div_cnt += 1
            number //= div
        if div_cnt != 0:
            factor[div] = div_cnt
        div += 1
    if number > 1:
        factor[number] = 1
    return factor

factors = factrization_prime(gcd)
print(len(factors) + 1)