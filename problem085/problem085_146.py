from collections import defaultdict
from math import gcd

N = int(input())
A = list(map(int, input().split()))
A_set = set(A)

num = 10 ** 6
primes = [0] * (num + 1)
primes[0] = 1
primes[1] = 1

for i in range(2, num + 1):
    if primes[i] != 0:
        continue

    cnt = 1
    while i * cnt <= num:
        primes[i * cnt] = i
        cnt += 1


def func(n):
    res_dic = defaultdict(int)
    while n > 1:
        x = primes[n]
        res_dic[x] += 1
        n //= x

    return res_dic


pairwise = True
cnt_dic = defaultdict(int)
for a in A:
    dic = func(a)

    for k in dic.keys():
        cnt_dic[k] += 1
        if cnt_dic[k] > 1:
            pairwise = False
            break

g = A[0]
for a in A[1:]:
    g = gcd(g, a)

if pairwise:
    print('pairwise coprime')
elif g == 1:
    print('setwise coprime')
else:
    print('not coprime')

