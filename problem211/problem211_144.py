import numpy as np

n,r = map(int,input().split())

if n < 10:
    print(r + 1000 - 100*n)
else:
    print(r)