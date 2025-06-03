#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import math

DEG60 = math.pi/3

def repl_edge(n, edges):
    # print('n=',n, 'edges=', len(edges))
    if n == 0:
        return edges
    new_list = list()
    for edge in edges:  # single tupple
        p1 = edge[0]
        p2 = edge[1]
        p_angle = edge[2]
        s = ((p1[0]*2+p2[0])/3, (p1[1]*2+p2[1])/3)
        t = ((p1[0]+p2[0]*2)/3, (p1[1]+p2[1]*2)/3)
        r = abs((t[0]-s[0])**2 + (t[1]-s[1])**2) ** 0.5
        angle = p_angle + DEG60
        u = (s[0] + math.cos(angle)*r, s[1] + math.sin(angle)*r)
        # print('r=', r, 'u=', u, 'angle=', angle)
        new_list += [(p1, s, p_angle), (s, u, p_angle+DEG60), \
                    (u, t, p_angle-DEG60), (t, p2, p_angle)]

    new_list = repl_edge(n-1, new_list)
    return new_list


n = int(sys.stdin.readline())
p1 = (0.0, 0.0)
p2 = (100.0, 0.0)
edges = [(p1, p2, 0.0)]

edges = repl_edge(n, edges)
for edge in edges:
    print(round(edge[0][0],6), round(edge[0][1],6))
print(round(edges[-1][1][0],6), round(edges[-1][1][1],6))

