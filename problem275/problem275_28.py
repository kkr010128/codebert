def p(n):
    if n == 1:
        return 300000
    elif n == 2:
        return 200000
    elif n == 3:
        return 100000
    else:
        return 0

x, y = map(int, input().split())
ans = 0
if x == y == 1:
    ans += 400000
ans += p(x) + p(y)
print(ans)
