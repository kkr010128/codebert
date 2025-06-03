import math
from decimal import *
import random
mod = int(1e9)+7

s = str(input())
n =len(s)
if(n%2==0):
    s1, s2 = s[:n//2], s[n//2:][::-1]
    ans =0
    for i in range(len(s1)):
        if(s1[i]!= s2[i]):
            ans+=1
    print(ans)
else:
    s1, s2 = s[:(n-1)//2], s[(n-1)//2:][::-1]
    ans = 0
    for i in range(len(s1)):
        if(s1[i]!= s2[i]):
            ans+=1
    print(ans)
