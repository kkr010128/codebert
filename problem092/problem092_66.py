

startX, countK, distanceD = map(int, input().split())
n = int(abs(startX) / distanceD)
ans = abs(startX) % distanceD
if n > countK:
    ans += distanceD * (n - countK)
else:
    if (countK - n) % 2 == 1:
        ans= abs(ans - distanceD)
print(ans)
