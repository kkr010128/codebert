import numpy as np

a = [[int(i) for i in input().split()] for _ in range(3)]
N = int(input())
b = [int(input()) for i in range(N)]

for bingo_num in b:
    for line in range(3):
        if bingo_num in a[line]:
            a[line][a[line].index(bingo_num)] =0

flag = False
for i in range(3):
    if a[i]==[0,0,0]:
        flag=True
    if a[0][i]==a[1][i]==a[2][i]==0:
        flag=True
if a[0][0]==a[1][1]==a[2][2]==0:
    flag = True
if a[2][0]==a[1][1]==a[0][2]==0:
    flag = True

print("Yes" if flag else "No")
