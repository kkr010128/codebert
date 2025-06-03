import math
n=int(input())
def koch(d,p1,p2):
	if d==0:
		return
	s=[0,0]
	t=[0,0]
	u=[0,0]
	s[0]=2/3*p1[0]+1/3*p2[0]
	s[1]=2/3*p1[1]+1/3*p2[1]
	t[0]=1/3*p1[0]+2/3*p2[0]
	t[1]=1/3*p1[1]+2/3*p2[1]
	u[0]=s[0]+(t[0]-s[0])*math.cos(math.pi/3)-(t[1]-s[1])*math.sin(math.pi/3)
	u[1]=s[1]+(t[0]-s[0])*math.sin(math.pi/3)+(t[1]-s[1])*math.cos(math.pi/3)
	koch(d-1,p1,s)
	print(*s)
	koch(d-1,s,u)
	print(*u)
	koch(d-1,u,t)
	print(*t)
	koch(d-1,t,p2)
print(0,0)
koch(n,[0,0],[100,0])
print(100,0)
