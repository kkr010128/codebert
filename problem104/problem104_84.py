read = lambda: list(map(int, input().split()))
l, r, d = read()
ans = 0
for i in range(l, r + 1):
    if i % d == 0:
        ans += 1
print(ans)