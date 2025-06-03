from math import gcd
K = int(input())
count = 0
for a in range(1,K+1):
    for b in range(1,K+1):
        l = gcd(a,b)
        for c in range(1,K+1):
            count += gcd(l,c)
print(count)