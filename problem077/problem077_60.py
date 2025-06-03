a, b, c, d = map(int, input().split())
L = [a*c, a*d, b*c, b*d]
ans = max(L)
print(ans)