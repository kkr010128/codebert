x, k, d = map(int, input().split())
x = abs(x)

if x >= k*d:
    ans = x - k*d
elif k&1:
    ans = min((x-d)%(2*d), 2*d - (x-d)%(2*d) )
else:
    ans = min(x%(2*d), 2*d - x%(2*d))

print(ans)