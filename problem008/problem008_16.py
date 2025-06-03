# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 10:56:33 2018

@author: maezawa
"""
n = int(input())
adj = [[] for _ in range(n)]
d = [0 for _ in range(n)]
f = [0 for _ in range(n)]

for j in range(n):
    ain = list(map(int, input().split()))
    u = ain[0]
    k = ain[1]
    for i in range(k):
        adj[u-1].append(ain[i+2]-1)
    adj[u-1].sort()
    #print(*adj[u-1])

t = 1

for j in range(n):
    if d[j] == 0:
        stack = [j]

    while stack:
        #print(stack)
        current = stack[-1]
        if d[current] == 0:
            d[current] = t
            t += 1
        flag = 0
        for k in adj[current]:
            if d[k] == 0:
                stack.append(k)
                flag = 1
                break
        if flag == 0:
            f[current] = t
            t += 1
            stack.pop()

    #print('current = {}, t = {}'.format(current, t))
    #print('stack', *stack)

for i in range(n):
    print('{} {} {}'.format(i+1, d[i], f[i]))

