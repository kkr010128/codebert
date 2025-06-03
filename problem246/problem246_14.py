from itertools import permutations
from bisect import bisect

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))
l = tuple(permutations(range(1, n + 1), n))
print(abs(bisect(l, p) - bisect(l, q)))