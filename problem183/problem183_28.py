import math
N=int(input())
if N==2:
  print(1)
  exit()
def yaku(n):
    a=set()
    s=int(math.sqrt(n))
    for i in range(2,s+1):
        if n%i==0:
            a.add(i)
            a.add(n//i)
    return a
ans=len(yaku(N-1))+1
a=yaku(N)
for i in a:
    n=N
    while n%i==0:
        n=n//i
    if n%i==1:
        ans+=1
print(ans+1)