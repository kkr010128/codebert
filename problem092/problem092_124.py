x, k, d = map(int, input().split())
x = abs(x)
num = x // d
if num >= k:
    ans = x - k*d
else:
    if (k-num)%2 == 0:
        ans = x - num*d
    else:
        ans = min(abs(x - num*d - d), abs(x - num*d + d))

print(ans)