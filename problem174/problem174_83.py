import math
K = int(input())
ans = 0
for i in range(1, K+1):
    for j in range(1, i+1):
        for k in range(1, j+1):
            gcd = math.gcd(i, math.gcd(j, k))
            if i == j == k:
                ans += gcd
            elif i != j and j != k:
                ans += 6 * gcd
            else:
                ans += 3 * gcd
print(ans)