N, K, S = map(int, input().split())

d = S
if S == int(1e9):
    d -= 1
else:
    d += 1

ans = [1 for _ in range(N)]
for i in range(N):
    if K > 0:
        ans[i] = S
        K -= 1
    else:
        ans[i] = d

print(*ans)
