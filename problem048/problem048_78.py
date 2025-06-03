import sys
import functools

def minmaxsum(*t):
    (x,y,z),e=t
    if x > e:
        x=e
    if y < e:
        y = e
    z += e
    return (x,y,z)

input()
m,x,s = functools.reduce(minmaxsum,map(int,input().split()),(1000000,-1000000,0\
))
print(m,x,s)