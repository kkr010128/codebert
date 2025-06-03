a, b, c, k = map(int, input().split())

ans = 0

ans += min(a, k)
k -= min(a, k)

k -= min(b, k)

ans -= min(c, k)

print(ans)
