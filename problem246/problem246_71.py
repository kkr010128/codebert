from itertools import permutations

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

perm = list(permutations(p))
perm.sort()
a = perm.index(p)
b = perm.index(q)
print(abs(a- b))
