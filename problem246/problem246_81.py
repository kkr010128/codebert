n=int(input())
P=[int(x) for x in input().split()]
Q=[int(x) for x in input().split()]
p=tuple(P)
q=tuple(Q)
l=list(range(1,n+1))
L=[]
import itertools
for v in itertools.permutations(l):
  L.append(v)
a=L.index(p)
b=L.index(q)
print(abs(a-b))