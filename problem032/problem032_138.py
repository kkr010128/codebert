from math import *


def distance (p,n,x,y):
    dis = 0.0
    if p == "inf":
        for i in range(0,n) :
            if dis < abs(x[i]-y[i]):
                dis = abs(x[i]-y[i])
    else :
        for i in range(0,n) :
            dis += abs(x[i]-y[i])**p
        dis = dis ** (1.0/p)
    return dis


if  __name__ == '__main__' :
     n = int(input())
     x = map(int,raw_input().split())
     y = map(int,raw_input().split())
     print distance(1,n,x,y)
     print distance(2,n,x,y)
     print distance(3,n,x,y)
     v = distance('inf',n,x,y)
     print "%.6f" % v