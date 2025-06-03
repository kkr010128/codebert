# coding: utf-8

import math

length = int(input())
total = 0
str = input()
table = list(str)
for i in range(length - 2):
    if table[i] == "A":
        if table[i+1] == "B":
            if table[i+2] == "C":
                total += 1

print(total)