import itertools


def LI():
    return tuple(map(int, input().split()))


N = int(input())
P = LI()
Q = LI()
Nlist = list(range(1, N+1))
count = 1
for v in itertools.permutations(Nlist, N):
    if P == v:
        p = count
    if Q == v:
        q = count
    count += 1
print(abs(p-q))
