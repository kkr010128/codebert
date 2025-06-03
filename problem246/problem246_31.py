import itertools
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
cnt, a, b = 0, 0, 0
for i in itertools.permutations(range(1, N+1)):
    if P == i:
        a = cnt
        if b != 0:
            break
    if Q == i:
        b = cnt
        if a != 0:
            break
    cnt += 1
print(abs(a-b))