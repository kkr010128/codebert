#! /usr/bin/env python
# -*- coding: utf-8 -*-

x_list = []
y_list = []
while True:
    x, y = map(int, raw_input().split())
    if x == 0 and y == 0:
        break
    else:
        x_list.append(x)
        y_list.append(y)

for i, num in enumerate(x_list):
    if x_list[i] == y_list[i]:
        print("%d %d") % (x_list[i], y_list[i])
    elif x_list[i] < y_list[i]:
        print("%d %d") % (x_list[i], y_list[i])
    else:
        print("%d %d") % (y_list[i], x_list[i])