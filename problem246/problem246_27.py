from itertools import permutations
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
r = 0
for i, x in enumerate(permutations([j for j in range(1,N+1)])):
    if x == P:
        r = abs(r-i)
    if x == Q:
        r = abs(r-i)
print(r)
