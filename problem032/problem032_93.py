import math
n=int(input())
x=[int(0) for i in range(n)]
y=[int(0) for i in range(n)]
x[:]=(int(a) for a in input().split())
y[:]=(int(a) for a in input().split())
p1=0
p2=0
p3=0
px=0
for i in range(n):
  p1+=abs(x[i]-y[i])
  p2+=abs(x[i]-y[i])**2
  p3+=abs(x[i]-y[i])**3
  if px<abs(x[i]-y[i]):
    px=abs(x[i]-y[i])

p2=math.sqrt(p2)
p3=p3**(1/3)

print('{:.05f}'.format(p1))
print('{:.05f}'.format(p2))
print('{:.05f}'.format(p3))
print('{:.05f}'.format(px))


