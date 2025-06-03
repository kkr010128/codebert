import math

k = int(input())
ans = 0
for h in range(1, k+1):
    for i in range(1, k+1):
        g = math.gcd(h, i)
        for j in range(1, k+1):
            ans += math.gcd(g, j)
print(ans)