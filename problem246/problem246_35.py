# author:  Taichicchi
# created: 12.09.2020 17:49:24

from itertools import permutations
import sys

N = int(input())

P = int("".join(input().split()))
Q = int("".join(input().split()))

perm = permutations([str(i) for i in range(1, N + 1)], N)

ls = []

for i in perm:
    ls.append(int("".join(i)))

print(abs(ls.index(P) - ls.index(Q)))
