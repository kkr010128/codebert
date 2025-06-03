a,b=map(int,input().split())
from fractions import *
g=gcd(a,b)
c=i=1
while g>1 and i*i<=g:
    i+=1
    if g%i==0:
        c+=1
    while g%i==0:
        g//=i
print(c+(g>1))