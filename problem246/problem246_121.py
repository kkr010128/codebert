import itertools
import math

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

arr = [i for i in itertools.permutations([i for i in range(1, n+1)])]

a = arr.index(p)
b = arr.index(q)
print(abs(a-b))
