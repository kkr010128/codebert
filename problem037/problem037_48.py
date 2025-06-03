# -*- coding: utf-8 -*-

S = int(raw_input())

h = S / 3600
S %= 3600
m = S / 60
S %= 60
s = S

print "%d:%d:%d" %(h, m, s)