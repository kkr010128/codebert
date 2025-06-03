a,b,c,k = map(int, input().split())

ans = min(a,k)
k -= min(a,k)

k -= min(b,k)

ans -= k
print(ans)

