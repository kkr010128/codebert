import sys
input()
for e in sys.stdin:
 a,b,c=sorted(map(int,e.split()))
 print(['NO','YES'][a*a+b*b==c*c])
