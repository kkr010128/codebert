# -*- coding: utf-8 -*-
# input
a, b = map(int, input().split())
x = list(map(int, input().split()))
print('Yes') if a <= sum(x) else print('No')