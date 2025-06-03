import math
cnt=0
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        wk=math.gcd(i,j)
        for k in range(1,n+1):
            cnt+=math.gcd(wk,k)
print(cnt)