# coding: utf-8
# Your code here!
# ITP1_3_C


while(True):
    x,y=map(int,input().split())
    if x == 0 and y == 0:
        break
    if x > y:
        print(y,x)
    else:
        print(x,y)
