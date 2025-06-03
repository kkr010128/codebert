import math
a,b=[int(i) for i in input().split()]
c=a//b
e=abs(a-(b*c))
f=abs(a-(b*(c+1)))
print(min(e,f))