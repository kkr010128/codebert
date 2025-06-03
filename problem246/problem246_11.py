from itertools import permutations

n = int(input())
p = [int(i) for i in input().split()]
q = [int(i) for i in input().split()]

perm = list(permutations(sorted(p), n))    #; print(perm)
a = perm.index(tuple(p))
b = perm.index(tuple(q))

print(abs(a-b))