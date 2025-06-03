#10_B
import math
a,b,C=map(int,input().split())
S=a*b*math.sin((C*2*math.pi)/360)/2
c=math.sqrt(a**2+b**2-2*a*b*math.cos((C*2*math.pi)/360))
L=a+b+c
h=2*float(S)/a
print(str(S)+'\n'+str(L)+'\n'+str(h)+'\n')
