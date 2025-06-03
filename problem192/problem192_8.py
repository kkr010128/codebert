N=int(input())
L=list(map(int,input().split()))
c={}
for i in set(L):
  c[i]=0
for i in L:
  c[i]+=1
s=sum([(i*(i-1))//2 for i in c.values()])
for i in L:
  print(s-c[i]+1)