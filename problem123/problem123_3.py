import math
from collections import defaultdict
ml=lambda:map(int,input().split())
ll=lambda:list(map(int,input().split()))
ii=lambda:int(input())
ip=lambda:list(input())
ips=lambda:input().split()

"""========main code==============="""

n=ii()
a=ll()
xor=0
for i in a:
    xor^=i
for i in a:
    print(xor^i,end=" ")