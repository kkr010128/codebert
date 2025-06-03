import math
n=int(input())
x=math.ceil(n/1.08)
if(math.floor(1.08*x)==n):
    ans=x
else:
    ans=str(":(")
print(ans)