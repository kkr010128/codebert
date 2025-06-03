N, M = map(int, input().split())
H = [int(x) for x in input().split()]
adj = [0] * N
good = [1]*N
for j in range(N):
    adj[j] = set()
for k in range(M):
    A, B = map(int, input().split())
    if H[A - 1] >= H[B - 1]:
        good[B - 1] = 0
    if H[A - 1] <= H[B - 1]:
        good[A - 1] = 0
print(sum(good))
