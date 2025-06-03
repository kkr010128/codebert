import itertools

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

A = list(itertools.permutations(range(1, N+1)))

for a in range(len(A)):
    if A[a] == P:
        p = a
    if A[a] == Q:
        q = a

print(abs(p - q))
