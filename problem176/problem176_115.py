# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

MOD = 10 ** 9 + 7
# gcdがNから順に数える、resetを用意、約数をそれぞれ引く

def make_divisors(n):  # nの約数を列挙
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

N, K = lr()
answer = 0
reset = [0] * (K+1)
for x in range(K, 0, -1):
    #gcdがx
    nums = K // x
    add = pow(nums, N, MOD)
    add -= reset[x]
    answer += add * x
    answer %= MOD
    divs = make_divisors(x)
    for d in divs:
        reset[d] += add

print(answer%MOD)
