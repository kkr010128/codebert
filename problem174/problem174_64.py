import math
k = int(input())
k += 1

ans = 0
for a in range(1, k):
    for b in range(1, k):
        for c in range(1, k):
            ans += math.gcd(a, math.gcd(b, c))

print(ans)