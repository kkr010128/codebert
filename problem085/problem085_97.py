import math
from functools import reduce
from collections import deque

N = int(input())
A = list(map(int, input().split()))


def gcd_list(numbers):
    return reduce(math.gcd, numbers)


max_A = max(A)

if max_A == 1:
    print('pairwise coprime')
    exit()
# エラトステネスの篩により素数を高速で求める
# そのかんにある数値がふるい落とされたその素数をメモしておく

D = [0] * (max_A + 1)
is_prime = [True] * (max_A + 1)
is_prime[0] = False
is_prime[1] = False
prime = deque()
for i in range(2, int(max_A ** 0.5) + 1):
    if not is_prime[i]:
        continue
    for j in range(i * 2, max_A + 1, i):
        is_prime[j] = False
        D[j] = i

for i in range(len(is_prime)):
    if is_prime[i]:
        D[i] = i

pairwise = True
check = [0] * (max_A + 1)
new_A = A[:]
for i in range(N):
    min_prime = D[new_A[i]]
    while True:
        if D[min_prime] == 0:
            break

        check[D[min_prime]] += 1
        while new_A[i] % min_prime == 0:
            new_A[i] //= min_prime

        min_prime = new_A[i]

        # print(check)


# print(D)
# print(check)

if max(check) > 1:
    pairwise = False
# print(check)
if pairwise:
    print('pairwise coprime')
else:
    if gcd_list(A) == 1:
        print('setwise coprime')
    else:
        print('not coprime')
