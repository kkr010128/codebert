#!/usr/bin/python3
# -*- coding: utf-8 -*-
h, w, m = map(int, input().split())
bom_set = set()
h_dict = {}
w_dict = {}
for i in range(m):
    hh, ww = map(int, input().split())
    bom_set.add(tuple([hh, ww]))
    if hh in h_dict:
        h_dict[hh] += 1
    else:
        h_dict[hh] = 1
    if ww in w_dict:
        w_dict[ww] += 1
    else:
        w_dict[ww] = 1
h_max_count = max(h_dict.values())
w_max_count = max(w_dict.values())
hh_dict = {}
ww_dict = {}
for hh in h_dict:
    if h_dict[hh] == h_max_count:
        hh_dict[hh] = h_max_count
for ww in w_dict:
    if w_dict[ww] == w_max_count:
        ww_dict[ww] = w_max_count
flag = 0
for hh in hh_dict:
    for ww in ww_dict:
        if tuple([hh, ww]) not in bom_set:
            flag = 1
            break
    if flag == 1:
        break
if flag == 1:
    print(h_max_count + w_max_count)
else:
    print(h_max_count + w_max_count - 1)