import math
ans = 0
num = int(input())
for i in range(1, num+1):
    for j in range(1, num+1):
        for k in range(1, num+1):
            ans += math.gcd(math.gcd(i, j),k)
print(ans)