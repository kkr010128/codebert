import itertools
N = int(input())
P=tuple(int(c) for c in input().split())
Q=tuple(int(c) for c in input().split())

l=list(c for c in itertools.permutations(range(1,N+1),N))
print(abs(l.index(P)-l.index(Q)))