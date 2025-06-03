a, b, c, k = map(int, input().split())
ans = 0
if a >= k:
    ans += k
    k = 0
else:
    ans += a
    k -= a
if b >= k:
    k = 0
else:
    k -= b
if c >= k:
    ans -= k
print(ans)