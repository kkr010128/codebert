import math
import numpy as np
from itertools import chain
count = 0
t = 0
a,b = map(int,input().split())

p = [list(map(int,input().split()))for i in range(a)]

fp = list(chain.from_iterable(p))

pp = np.abs(fp)

for i in range(a):
    s = math.sqrt(pp[t]**2 + pp[t+1]**2)
    t +=2
    if s <= b:
        count+=1
print(count)