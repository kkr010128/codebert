# coding: utf-8
N = list(map(int,list(input())))

sN = sum(N)

if sN%9 ==0:
    print("Yes")
else:
    print("No")
