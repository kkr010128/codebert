#coding:utf-8
#1_3_C 2015.3.24
while True:
    x,y = map(int,input().split())
    if (x,y) == (0,0):
        break
    elif x > y:
        x,y = y,x
    print('{} {}'.format(x,y))