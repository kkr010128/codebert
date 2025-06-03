a, b, c, d = map(int,input().split())
inf = -10**9
ans = max(a*c, a*d)
ans = max(ans, b*c)
ans = max(ans, b*d)
print(ans)