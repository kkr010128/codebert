N, D = map(int, input().split())
XY = [list(map(int, input().split())) for i in range(N)]
ans = 0
for i in range(N):
    if (XY[i][0]**2 + XY[i][1]**2)**0.5 <= D:
        ans += 1
print(ans)