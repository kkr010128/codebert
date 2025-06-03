from collections import defaultdict

G = defaultdict(set)
N, M = [int(_) for _ in input().split()]
for _ in range(M):
    A, B = [int(_) for _ in input().split()]
    G[A].add(B)
    G[B].add(A)

f = [-1 for _ in range(N+1)]
f[1] = 0

pool = set([1])
np = set()
cnt = 0
while pool:
    np = set()
    for p in pool:
        for v in G[p]:
            if f[v] == -1:
                f[v] = p
                cnt += 1
                np.add(v)
    pool = np

print("Yes")
for i in range(2, N+1):
    print(f[i])
