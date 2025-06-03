rs = [(x - l, x + l) for x, l in (map(int, input().split()) for _ in range(int(input())))]
rs.sort(key=lambda x: x[1])
last = - 10 ** 9
ans = 0
for l, r in rs:
    if last <= l:
        ans += 1
        last = r
print(ans)