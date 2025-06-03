import sys
import math

n = (int)(input())
money = 100000.0

for i in range(n):
    money = math.ceil(money * 1.05 / 1000) * 1000
print((int)(money))