# -*- coding: utf-8 -*-

while True:

    line = list(input())

    if '-' in line:
        break

    m = int(input())
    for i in range(m):
        h = int(input())
        for j in range(h):
            line.append(line[0])
            line.pop(0)

    for i in range(len(line)):
        print(line[i],end='')
    print()
