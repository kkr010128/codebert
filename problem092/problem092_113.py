x, k, d = map(int, input().split())

ax = abs(x)
n = ax // d
if n >= k:
    ans = ax - k*d
else:
    a = ax - n*d
    if (k - n) % 2:
        ans = abs(a - d)
    else:
        ans = abs(a)

print(ans)
