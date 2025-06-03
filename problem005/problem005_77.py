import sys
for l in sys.stdin:
 x,y=map(int, l.split())
 m=x*y
 while x%y:x,y=y,x%y
 print "%d %d"%(y,m/y)