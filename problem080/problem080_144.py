n=int(input())
s,p=10**100,10**100
t,q=-1000000000000,-1000000000000

for i in range(n):
  x,y=map(int,input().split())
  s=min(s,x+y)
  t=max(t,x+y)
  p=min(p,x-y)
  q=max(q,x-y)
  
print(max(t-s,q-p))
