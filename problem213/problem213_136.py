from numpy import average
from decimal import Decimal, ROUND_HALF_UP
 
n=int(input())
x=list(map(int,input().split()))
 
p=Decimal(str(average(x))).quantize(Decimal('1'),rounding=ROUND_HALF_UP)
 
ans=0
for i in x:
	ans+=((i-p)**2)

print(ans)