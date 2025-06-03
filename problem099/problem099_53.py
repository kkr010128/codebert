n,k=map(int,input().split())
a=list(map(int,input().split()))
import math
x=0
y=10**9
z=5*(10**8)
s=0
for i in range(100):
    t=0
    for j in range(n):
        t+=a[j]//z
    if t<=k:
        s=t
        y=z
        z=(x+y)/2
    else:
        x=z
        z=(x+y)/2
print(math.ceil(z))
