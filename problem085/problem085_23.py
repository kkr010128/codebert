import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
from functools import reduce
from math import gcd
def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    if reduce(gcd, A) != 1:
        print("not coprime")
        return

    M = max(A)
    sieve = list(range(M + 1))
    primes = []

    for i in range(2, M + 1):
        if sieve[i] == i:
            primes.append(i)
        j = 0
        for p in primes:
            if not (p <= sieve[i] and i * p <= M):
                break
            sieve[i * p] = p

    used = set()
    for a in A:
        primes = set()
        while a > 1:
            p = sieve[a]
            primes.add(p)
            a //= p
        for p in primes:
            if p in used:
                print("setwise coprime")
                return
            used.add(p)

    print("pairwise coprime")
resolve()