x, k, d = map(int, input().split())

x = abs(x)

if x - k * d > 0:
    ans = x - k * d
else:
    if (k - x // d) % 2 == 0:
        ans = x - d * (x // d)
    else:
        ans = abs(x - d * (x // d) - d)

print(ans) 
