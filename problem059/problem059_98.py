# -*- coding: utf-8 -*-
r,c = [int(a) for a in input().split(' ')]
arr = []
Hsum=0
for x in range(r):
    i =[int(a) for a in input().split(' ')]
    i.append(sum(i))
    arr.append(i)
arr2=[]
for y in range(c+1):
    for z in range(r):
        Hsum += arr[z][y]
    arr2.append(Hsum)
    Hsum=0
arr.append(arr2)

for y in range(r+1):
    for z in range(c+1):
        if z == c:
            print(arr[y][z])
        else:
            print(arr[y][z],end = " ")