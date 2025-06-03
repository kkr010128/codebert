n,m=map(int, input().split())

a=[int(x) for x in input().split()]

kaisuu=0

for i in a:
    zantei=0
    while True:
        if i%2==0:
            zantei+=1
            i//=2
        else:
            break
    if kaisuu==0:
        kaisuu=zantei
    else:
        if kaisuu!=zantei:
            print(0)
            exit()

sks=a[0]//2

import math

for i in range(1,len(a)):
    sks=sks*(a[i]//2)//(math.gcd(sks,a[i]//2))

ans=int(m/(2*sks)+(1/2))

print(ans)