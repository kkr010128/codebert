from functools import reduce
from math import gcd 

n = int(input())
A = list(map(int, input().split()))

def furui(x):
    memo = [0]*(x+1)
    primes = []
    for i in range(2, x+1):
        if memo[i]: continue
        primes.append(i)
        memo[i] = i
        for j in range(i*i, x+1, i):
            if memo[j]: continue
            memo[j] = i
    return memo, primes

memo, primes = furui(10**6+5)

pr = [True]*(10**6+5)
for a in A:
    if a == 1: continue
    while a != 1:
        w = memo[a]
        if not pr[w]:
            break
        pr[w] = False
        while a%w == 0:
            a = a // w
    else:
        continue
    break
else:
    print('pairwise coprime')
    exit()

if reduce(gcd, A) == 1:
    print('setwise coprime')
else:
    print('not coprime')
