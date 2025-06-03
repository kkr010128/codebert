a, b, c, d = map(int, input().split())
ans = 10**20 * -1
ans = max(ans, a * c)
ans = max(ans, a * d)
ans = max(ans, b * c)
ans = max(ans, b * d)
print(ans)
