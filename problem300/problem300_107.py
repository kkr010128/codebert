import math
n,m=map(int,input().split())
gcd=math.gcd(m,n)
i=1
ans=[]
max=int(math.sqrt(gcd))
for i in range(2,max+2):
    while gcd%i==0:
        ans.append(i)
        gcd//=i
if gcd>1:
  ans.append(n)

print(len(set(ans))+1)