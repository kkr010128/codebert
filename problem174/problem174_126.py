import math
K = int(input())
sum = 0
for i in range(1,K+1):
    for j in range(1,K+1):
        for k in range(1,K+1):
            gcd_1 = math.gcd(i,j)
            sum = sum + math.gcd(gcd_1,k)
print(sum)