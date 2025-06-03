import math
n,m=map(int,input().split())
a=list(map(int,input().split()))
half_a=[ai//2 for ai in a]
# print(half_a)
lcm=half_a[0]
for i in range(n-1):
    a,b=lcm,half_a[i+1]
    lcm=a*b//math.gcd(a,b)
# print(lcm)
pow_cnt=0
tmp=half_a[0]
while tmp%2==0:
    pow_cnt+=1
    tmp=tmp//2
flag=True
for ai in half_a[1:]:
    if ai%(2**pow_cnt)!=0:
        flag=False
        break
    elif  ai%(2**(pow_cnt+1))==0:
        flag=False
        break
if flag:
    print(math.ceil(m//lcm/2))
else:
    print(0)