from itertools import permutations
from bisect import bisect_left

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

perm = list(permutations(p))
perm.sort()
a = bisect_left(perm, p)
b = bisect_left(perm, q)

print(abs(a- b))
