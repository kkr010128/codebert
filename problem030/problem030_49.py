from math import *
a,b,C=map(int,input().split())
C=C*pi/180
S=a*b*sin(C)/2
print(S,a+b+(a*a+b*b-2*a*b*cos(C))**0.5,2*S/a,sep='\n')