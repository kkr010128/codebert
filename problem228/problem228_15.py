#!/usr/bin/env python3

H = int(input())

i = 1
while H >= 2**i:
    i += 1

ans = 0
for x in range(i):
    ans += 2 ** x
    
print(ans)
