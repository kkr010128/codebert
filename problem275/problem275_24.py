# -*- coding: utf-8 -*-
a = list(map(int, input().split()))

ans = 0
for i in a:
    if i == 1:
        ans += 300000
    elif i == 2:
        ans += 200000
    elif i == 3:
        ans += 100000
    
if a[0] == a[1] == 1:
    ans += 400000

print(ans)