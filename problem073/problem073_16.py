import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
from collections import Counter
def resolve():
    n = int(input())

    sieve = list(range(n + 1))
    primes = []
    for i in range(2, n + 1):
        if sieve[i] == i:
            primes.append(i)
        for p in primes:
            if p * i > n or sieve[i] < p:
                break
            sieve[p * i] = p

    ans = 0
    for i in range(1, n):
        C = Counter()
        while i > 1:
            C[sieve[i]] += 1
            i //= sieve[i]
        score = 1
        for val in C.values():
            score *= val + 1
        ans += score
    print(ans)
resolve()