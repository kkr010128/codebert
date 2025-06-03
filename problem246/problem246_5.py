import itertools

N = int(input())
P = tuple(map(int,input().split()))
Q = tuple(map(int,input().split()))

perm = list(itertools.permutations(range(1,N+1)))
for i in range(len(perm)):
    if P == perm[i]:
        a = i
    if Q == perm[i]:
        b = i

print(abs(a-b))
