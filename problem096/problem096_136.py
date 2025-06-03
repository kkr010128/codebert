N, D = [int(v) for v in input().split()]
D = D*D
ans = 0
for _ in range(N):
    x, y = [int(v) for v in input().split()]
    if (x**2 + y**2) <= D:
        ans += 1

print(ans)