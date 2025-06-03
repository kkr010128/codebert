from itertools import groupby
s=input()
if s[0]=='>':
  s='<'+s
g=groupby(s)
a=[]
for i,j in g:
  a.append(len(list(j)))
def sum(n):
  return n*(n+1)//2
x=0
if len(a)%2==1:
  a+=[1]
for i in range(0,len(a),2):
  x+=sum(min(a[i],a[i+1])-1)
  x+=sum(max(a[i],a[i+1]))
print(x)
