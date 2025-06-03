N=int(input())
import math
n=int(math.sqrt(N))
m=0
T=True
while T==True:
  if N%n==0:
    m=N//n
    T=False
    break
  else:
    n-=1
print(n+m-2)