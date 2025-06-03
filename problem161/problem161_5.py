from math import floor
a, b, n = map(int, input().split())

ans = floor(min(n, b-1)*a/b)
print(ans)