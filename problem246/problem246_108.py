from itertools import permutations
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
M = []
for i in range(N):
    M.append(i+1) 
p, q = 0, 0
for i, n in enumerate(list(permutations(M))):
    if n == P:
        p = i
    if n == Q:
        q = i
print(abs(p - q))