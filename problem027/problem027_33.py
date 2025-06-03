from math import *
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def div3(a,b):
    c1=(2*a+b)/3
    c2=(a+2*b)/3
    return [c1,c2]

def main():
    n=int(input())
    xy=[[0,0],[100,0]]
    #aa=list(map(int, input().split()))
    for _ in range(n):
        nxy=[[0,0]]
        for [x0,y0],[x4,y4] in zip(xy,xy[1:]):
            x1,x3=div3(x0,x4)
            y1,y3=div3(y0,y4)
            a=((x3-x1)**2+(y3-y1)**2)**0.5
            rad=atan2(y3-y1,x3-x1)
            x2=x1+a*cos(rad+pi/3)
            y2=y1+a*sin(rad+pi/3)
            nxy+=[[x1,y1],[x2,y2],[x3,y3],[x4,y4]]
        xy=nxy
    for x,y in xy:
        print(x,y)

main()

