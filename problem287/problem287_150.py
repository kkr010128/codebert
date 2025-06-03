# -*- coding: utf-8 -*-

N = int(input())

ans ='No'
for x in range(1, 10, 1):
    if (N % x) == 0:
        for y in range(x, 10, 1):
            if x * y == N:
                ans = 'Yes'
                break
    
    if ans == 'Yes':
        break

print(ans)