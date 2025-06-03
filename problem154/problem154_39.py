import itertools
n,k=map(int,input().split())

d=[]
a=[]

for i in range(k):
  p=int(input())
  d.append(p)
  q=list(map(int,input().split()))
  a.append(q)

c=list(itertools.chain.from_iterable(a))
c.sort()

c_set=set(c)
c=list(c_set)

print(n-len(c))