import math
k = int(input())
ans = 0
for q in range(1,k+1):
    for r in range(1,k+1):
        x = math.gcd(q,r)
        for s in range(1,k+1):
            ans += math.gcd(x,s)

print(ans)
