from collections import *
n=int(input())
l=[]
for i in range(n):
    l.append(input())
c=Counter(l)
m=max(c.values())
d=[]
for i in c:
    if(c[i]==m):
        d.append(i)
d.sort()
for i in d:
    print(i)
