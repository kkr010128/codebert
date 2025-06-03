from itertools import permutations as perm
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

comb = list(perm(range(1, N+1)))
def find(x):
    for i, n in enumerate(comb):
        if x == n:
            return i
a = find(P)
b = find(Q)
ans = abs(a - b)
print(ans)