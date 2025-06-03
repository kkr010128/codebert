# -*- coding: utf-8 -*-
n = int(input())
a = [int(i) for i in input().split()] 

su = [0 for _ in range(n)] #鉄の棒の切れ目の座標
for i in range(n):
    su[i] = su[i-1] + a[i]
#print(su)

tmp = 2 * pow(10, 10) + 1
for i in su:
    #if abs(i - su[-1]/2) < tmp:
    #    tmp = abs(i - su[-1]/2)
    tmp = min(tmp, abs(i - su[-1]/2))
#print(su[-1]/2, tmp)

"""
#中心に一番近い鉄の棒の切れ目と中心との距離の差
l = 0
r = n-1
while (l - r) >= 1:
    c = (l + r) // 2
    #print(l, r, c)
    if su[c] < su[-1] / 2:
        l = c
    elif su[c] > su[-1] / 2:
        r = c
#print(su[l], su[r])
tmp = min(abs(su[l] - su[-1]/2), abs(su[r] - su[-1]/2))
print(tmp)
"""

ans = 2 * tmp
print(int(ans))
