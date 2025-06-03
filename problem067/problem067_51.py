#coding: utf-8

p = [0,0]
n = int(input())
for i in range(n):
    c1 = input().split(" ")
    c2 = sorted(c1)

    if c1[0] == c1[1]:
        p[0] += 1
        p[1] += 1

    elif c1[0] == c2[0]:
        p[1] += 3
    else:
        p[0] += 3

print(str(p[0]) + " " + str(p[1]))
