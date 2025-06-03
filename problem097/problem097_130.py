import time
start=time.time()
k=int(input())
ans=0
x=k
for i in range(10**9):
  while x%10!=7:
    x+=k
    if time.time()-start>=1.9:exit(print(-1))
  x//=10
  if x==0:exit(print(i+1))
