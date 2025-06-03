def li():
    return [int(x) for x in input().split()]

N = int(input())
A = li()

import math
from functools import reduce
from collections import defaultdict

# 最大公約数（リスト引数）
# 空のリストを渡さないよう注意
def GCD_list(numbers):
    return reduce(math.gcd, numbers)



# 数列全ての高速素因数分解
MAX = 10 ** 6
is_prime = [True] * (MAX + 1)
divs = [1] * (MAX + 1)
is_prime[0], is_prime[1] = False, False
i = 1
while i * i <= MAX:
    if not is_prime[i]:
        i += 1
        continue
    for j in range(2 * i, MAX + 1, i):
        is_prime[j] = False
        divs[j] = i
    i += 1

pairwise_coprime = True
all_primes = defaultdict(int)
for k in range(N):
    n = A[k]
    p = divs[n]
    primes = defaultdict(int)
    while p > 1:
        primes[p] += 1
        n = n // p
        p = divs[n]
    # 最後に残った数は1か素数にしかならない
    if n != 1:
        primes[n] += 1
    for key in primes:
        if all_primes[key] > 0 and primes[key] > 0:
            pairwise_coprime = False
            break
        all_primes[key] += primes[key]

gcd = GCD_list(A)
setwise_comprime = (gcd == 1)
if pairwise_coprime:
    print('pairwise coprime')
elif setwise_comprime:
    print('setwise coprime')
else:
    print('not coprime')