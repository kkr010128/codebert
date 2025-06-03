import sys
import math
from enum import Enum

while True:
    n=int(input())
    if n==0:
        break
    s=list(map(int,input().split()))
    
    sum1=0
    for i in range(len(s)):
        sum1+=s[i]
    a=sum1/len(s)
    
    sum2=0
    for i in range(len(s)):
        sum2+=s[i]*s[i]
    b=sum2/len(s)
    
    print("%.10f"%(math.sqrt(b-a*a)))
