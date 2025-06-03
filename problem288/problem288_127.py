import math
n=int(input())

i=1
ans=10**20

while i*i<=n:
    if n%i==0:
        x=i
        y=n//i
        ans=min(ans,x+y-2)
    
    i+=1
print(ans)