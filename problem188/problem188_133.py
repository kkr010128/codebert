X,Y,A,B,C=map(int,input().split())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
r=list(map(int,input().split()))
p.sort()
p.reverse()
q.sort()
q.reverse()
while len(p)>X:
  p.pop()
while len(q)>Y:
  q.pop()
s=p+q+r
s.sort()
s.reverse()
c=0
for i in range(X+Y):
  c+=s[i]
print(c)