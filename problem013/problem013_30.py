# -*- coding: utf-8 -*-

n = int(raw_input())
R_List = []
Max = 0
R_min = 0
for i in range(n):
    R_List.append(int(raw_input()))
    if i == 0:
        R_min = R_List[0]
    elif i == 1:
        Max = R_List[1]-R_min
        R_min = min(R_min, R_List[1])
    else:
        Max = max(Max, R_List[i]-R_min)
        R_min = min(R_min, R_List[i])
print Max