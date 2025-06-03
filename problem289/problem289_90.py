import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


a,b,x = list(map(int, input().split()))
import math
if x*2>=a*a*b:
    the = (a*b - x/a) / (0.5*a*a)
else:
    the = (b*b*a) / (2*x)
ans = math.atan(the)
print(ans*180/math.pi)