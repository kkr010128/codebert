A, B = map(int, input().split())

Xbmin = 10 * B
Xbmax = 10 * B + 10
ans = -1

for x in range(Xbmin, Xbmax):
    if 100 * A <= x * 8 and x * 8 < 100 * (A + 1):
        ans = x
        break
    
print(ans)