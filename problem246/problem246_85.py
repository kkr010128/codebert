from math import factorial
from itertools import permutations

n = int(input())
p = tuple(map(str, input().split()))
q = tuple(map(str, input().split()))

num = [str(i) for i in range(1, n+1)]

allnum = list(i for i in permutations(num, n))

print(abs(allnum.index(p) - allnum.index(q)))