#!/usr/bin/env python

def GCD(x,y):
    while y!=0:
        tmp=y
        y=x%y
        x=tmp
    return x

if __name__ == "__main__":
    x,y=list(map(int,input().split()))
    if x<y:
        tmp=x
        x=y
        y=tmp
    print(GCD(x,y))