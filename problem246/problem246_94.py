import itertools

n = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

Psort = sorted(P)
Pp = list(itertools.permutations(Psort))

a = Pp.index(P)
b = Pp.index(Q)

print(abs(a-b))