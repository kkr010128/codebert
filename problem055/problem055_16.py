#!/usr/bin/env python3

n = int(input())
matrix = []
while n > 0:
    values = [int(x) for x in input().split()]
    matrix.append(values)
    n -= 1

official_house = [[[0 for z in range(10)] for y in range(3)] for x in range(4)]

Min = 0
Max = 9
for b, f, r, v in matrix:
    num = official_house[b - 1][f - 1][r - 1]
    if Min >= num or Max >= num:
        official_house[b - 1][f - 1][r - 1] += v

for i in range(4):
    for j in range(3):
        print('',' '.join(str(x) for x in official_house[i][j]))
    if 3 > i:
        print('#' * 20)