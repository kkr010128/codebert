n, d = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in xy:
    if (i[0]**2 + i[1]**2)**(1/2) <= d:
        ans += 1
print(ans)
