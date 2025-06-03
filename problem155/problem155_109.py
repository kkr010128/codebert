N, M = map(int,input().split())
H = list(map(int,input().split()))
MAX = [0 for _ in range(N)]
for _ in range(M):
    a, b = map(int,input().split())
    MAX[a-1] = max(MAX[a-1],H[b-1])
    MAX[b-1] = max(MAX[b-1],H[a-1])

ans = 0
for i in range(N):
    if H[i] > MAX[i]:
        ans += 1

print(ans)

