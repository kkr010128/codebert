from math import gcd
k=int(input())
ans = 0
for a in range(1,k+1):
    for b in range(1,k+1):
        gab=gcd(a,b)
        for c in range(1,k+1):
            ans+=gcd(gab,c)
print(ans)