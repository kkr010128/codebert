N, M = map(int, input().split())
H = list(map(int, input().split()))
max_h = [0]*N
ans = 0
for i in range(M):
    a, b = map(int, input().split())
    max_h[a-1] = max(max_h[a-1], H[b-1])
    max_h[b-1] = max(max_h[b-1], H[a-1])
for j in range(N):
    if max_h[j] < H[j]:
       ans += 1
print(ans)
