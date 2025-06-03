# -*- coding: utf-8 -*-

n = int(input())
t_point, h_point = 0, 0

for i in range(n):
    t_card,  h_card  = map(str, input().split())

    if t_card == h_card:
        t_point += 1
        h_point += 1
    elif t_card > h_card:
        t_point += 3
    elif t_card < h_card:
        h_point += 3

print('{0} {1}'.format(t_point, h_point))
