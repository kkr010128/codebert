# coding: utf-8
# Your code here!
# ITP1_5_A

while(True):
    x,y=map(int,input().split())
    if x==0 and y==0:
        break
    else:
        for r in range(0,x): 
            print("#"*y)
        print("")
