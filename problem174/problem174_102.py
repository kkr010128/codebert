k = int(input())

sum = 0

def gcd(x, y): # ユークリッドの互除法
    if y > x:
        y,x = x,y
    while y > 0:
        r = x%y
        x = y
        y = r
    return x

import math

for i in range(1,k+1):
    for m in range(1,k+1):
        sub = gcd(i,m)
        for l in range(1,k+1):
            sum += gcd(sub,l)
print(sum)
