# -*- coding: utf-8 -*-
A_ele = []
B_ele = []
C_ele = []
ele = [int(x) for x in input().split()]
for i in range(ele[0]):
    A_ele.append([int(x) for x in input().split()])
for i in range(ele[1]):
    B_ele.append([int(x) for x in input().split()])
for i in range(ele[0]):
    C_ele.append([])
    for j in range(ele[1]):
        for k in range(ele[2]):
            if j == 0:
                C_ele[i].append(0)
            C_ele[i][k] = C_ele[i][k] + A_ele[i][j] * B_ele[j][k]
for i in range(ele[0]):
    print(' '.join(map(str,C_ele[i])))
