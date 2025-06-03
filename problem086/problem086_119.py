n, x, t = map(int, input().split())
ans = t*(n//x)
if n % x != 0:
    ans += t

print(ans)