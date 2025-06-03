#! /usr/bin/env python
# -*- coding: utf-8 -*-

x_list = []
while True:
    x = int(raw_input())
    if x == 0:
        break
    else:
        x_list.append(x)

for i, x in enumerate(x_list, 1):
    print("Case %d: %d") % (i, x)