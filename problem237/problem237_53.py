# -*- coding: utf-8 -*-

N = int(input().strip())
XL_list = [list(map(int, input().rstrip().split())) for i in range(N)]
#-----

section = []

for X,L in XL_list:
    section.append( ( X - L , X + L ) )


section.sort(key= lambda x: x[1])
prev_tail = -float("inf")
cnt = 0

for left,right in section:
    if prev_tail <= left:
        cnt += 1
        prev_tail = right
        

print(cnt)
