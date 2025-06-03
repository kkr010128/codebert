import sys

a,b = map(int, sys.stdin.readline().split())

x=int(a//b)
y=int(a%b)
z=float(a/b)

print (x,y,"{0:2f}".format(z))