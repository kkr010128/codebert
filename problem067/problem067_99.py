# coding: utf-8
# Your code here!

n = int(input())
ta = 0
ha = 0
for i in range(n):
    a, b = list(input().split())
    if a == b:
        ta += 1
        ha += 1
    elif a > b:
        ta += 3
    else:
        ha += 3
print(ta,ha)
