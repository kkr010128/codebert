import itertools
N = int(input())
P = tuple(map(int,input().split()))
Q = tuple(map(int,input().split()))
l = []
for i in range(1,N+1):
    l.append(i)
tmp = sorted(list(itertools.permutations(l)))

p = tmp.index(P)
q = tmp.index(Q)
print(abs(p-q))