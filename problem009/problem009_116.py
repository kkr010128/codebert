n = int(input())
G = {}
D = [-1] * n
for _ in range(n):
    A = list(map(int, input().split()))
    G[A[0] - 1] = [a - 1 for a in A[2:]]

# print(G)

q = [(0, 0)]
while len(q) > 0:
    v, d = q[0]
    del q[0]
    if D[v] >= 0:
        continue
    D[v] = d

    for nv in G[v]:
        q.append((nv, d+1))

for i in range(n):
    print(i+1, D[i])

