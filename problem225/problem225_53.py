import math 
import sys 
#t=int(sys.stdin.readline())
t=1
for _ in range(t):
    n,m=map(int,input().split())
    print(math.ceil(n/m))
