from sys import stdin,stdout
LI=lambda:list(map(int,input().split()))
MAP=lambda:map(int,input().split())
IN=lambda:int(input())
S=lambda:input()
import math
from collections import Counter,defaultdict


n=IN()
a=LI()
ans=0
for i in range(n):
    ans^=a[i]
for i in range(n):
    print(ans^a[i],end=" ")
