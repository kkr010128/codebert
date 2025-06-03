# coding: utf-8
# Your code here!
import sys
import math
n=int(input())
ans=n
for i in range(1,int(math.sqrt(n))+1):
    if n%i==0:
        a=i
        b=int(n/i)
        if a+b-2<ans:
            ans=a+b-2
print(ans)
    
