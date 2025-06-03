import math
K = int(input())
total = 0
for x in range(1, K+1):
    for y in range(1, K+1):
        for z in range(1, K+1):
            total = total+math.gcd(x, math.gcd(y, z))
print(total)
