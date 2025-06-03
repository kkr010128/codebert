import math
a,b,c=map(int,input().split())
C=(c/180)*math.pi
S=(a*b*math.sin(C))/2
L=a+b+(a**2+b**2-2*a*b*math.cos(C))**0.5
h=b*math.sin(C)
print("%.5f\n%.5f\n%.5f\n"%(S,L,h))