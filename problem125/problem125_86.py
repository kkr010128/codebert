import sys
import math
import numpy as np
import functools
import operator
import collections
import itertools

X=int(input())
ans=1
for i in range(1,100000):
    if (X*i)%360==0:
        print(ans)
        sys.exit()
    ans+=1