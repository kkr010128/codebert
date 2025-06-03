from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# 素因数分解、リストで返す
#############################################################
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    a.sort()
    return a
#############################################################

primes = defaultdict(int)

for i in range(N):
    p = prime_factorize(A[i])
    p_set = set(p)
    for pi in p_set:
        primes[pi] += 1

# 全て1の時、primesが空になってmaxが取れない
if len(primes) == 0:
    print("pairwise coprime")
    exit()

max_cnt = max(primes.values())
# min_cnt = min(primes.values())

if max_cnt == 1:
    print("pairwise coprime")
elif max_cnt != N:
    print("setwise coprime")
else:
    print("not coprime")
