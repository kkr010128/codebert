# Comparing Strings
a, b = map(int, input().split())
a, b = min(a, b), max(a, b)
ans = ''.join([str(a) for e in range(b)])
print(ans)
