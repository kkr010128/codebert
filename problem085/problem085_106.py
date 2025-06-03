import functools
from math import gcd
N = int(input())
A = list(map(int, input().split()))
MAX = 10 ** 6 + 10

if functools.reduce(gcd, A) != 1:
    print("not coprime")
    exit()

prime_list = [i for i in range(MAX + 1)]
p = 2
while p * p <= MAX:
    if prime_list[p] == p:
        for q in range(2*p, MAX+1, p):
            if prime_list[q] == q:
                prime_list[q] = p
    p += 1

prime = set()
for a in A:
    tmp = set()
    while a > 1:
        tmp.add(prime_list[a])
        a //= prime_list[a]
    for p in tmp:
        if p in prime:
            print("setwise coprime")
            exit()
        prime.add(p)
else:
    print("pairwise coprime")
