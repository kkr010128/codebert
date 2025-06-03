import math

K = int(input())
ans = 0

A = {}
for a in range(1, K+1):
    A[a] = 0

for a in range(1, K+1):
    for b in range(1, K+1):
        num = math.gcd(a, b)
        A[num] += 1

for c in range(1, K+1):
    for k in A.keys():
        num = math.gcd(c, k) * A[k]
        ans += num

print(ans)