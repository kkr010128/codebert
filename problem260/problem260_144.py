import math
from collections import defaultdict
ml=lambda:map(float,input().split())
ll=lambda:list(map(int,input().split()))
ii=lambda:int(input())
ip=lambda:list(input())

"""========main code==============="""

a,b,c=ml()
if(a+b+c>=22):
    print("bust")
else:
    print("win")