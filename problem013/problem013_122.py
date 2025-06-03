# -*- coding: utf-8 -*-
num = int(raw_input())
a = int(raw_input())
b = int(raw_input())
diff = b - a
pre_min = min(a,b)

counter = 2
while counter < num:
    current_num = int(raw_input())
    if diff < current_num - pre_min:
        diff = current_num - pre_min
    if pre_min > current_num:
        pre_min = current_num
    counter += 1

print diff