n, d = [int(s) for s in input().split()]
d2 = d ** 2
ans = 0
for _ in range(n):
    x, y = [int(s) for s in input().split()]
    if x ** 2 + y ** 2 <= d2:
        ans += 1
print(ans)