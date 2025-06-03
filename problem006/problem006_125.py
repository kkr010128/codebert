# -*- coding: utf-8 -*-

week = int(raw_input())
debt = 100000
for i in range(week):
    debt = debt*1.05
    if debt%1000 != 0:
        debt -= debt%1000
        debt += 1000
print(int(debt))