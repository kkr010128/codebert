# -*- coding:utf-8 -*-

n = int(input())

for i in range(2,n+1):
    a = i // 10
    a = a % 10
    b = i // 100
    b = b % 10
    if i % 3 == 0:
        print(' ',i,sep='',end='')
    elif i % 10 == 3:
        print(' ',i,sep='',end='')
    elif a == 3:
        print(' ',i,sep='',end='')
    elif i // 100 == 3:
        print(' ',i,sep='',end='')
    elif i // 1000 == 3:
        print(' ',i,sep='',end='')
    elif i // 10000 == 3:
        print(' ',i,sep='',end='')
    elif b == 3:
        print(' ',i,sep='',end='')
print('')