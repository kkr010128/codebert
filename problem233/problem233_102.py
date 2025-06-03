N = int(input())
P = tuple(map(int, input().split()))
minp = P[0]
ans = 1
for i in range(1, N):
    if P[i] <= minp:
        ans += 1
    minp = min(minp, P[i])
print(ans)