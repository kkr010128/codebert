N, M = map(int, input().split())
H = list(map(int, input().split()))
count = [0]*N
ans = 0
for _ in range(M):
    a, b = map(int, input().split())
    if H[a-1] > count[b-1]:
        count[b-1] = H[a-1]
    if H[b-1] > count[a-1]:
        count[a-1] = H[b-1]
for i in range(N):
    if H[i] > count[i]:
        ans += 1
print(ans)