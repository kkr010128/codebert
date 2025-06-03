# coding: utf-8

x,y=map(int,input().split())

while not(x==0 and y==0):
    if x>y:
        x,y=y,x
    print(str(x)+" "+str(y))

    x,y=map(int,input().split())