# -*- coding: utf-8 -*-
def check(r,g,b):
    if g > r and b > g:
        return True
    else:
        return False

A,B,C = map(int, input().split())
K = int(input())

for i in range(K+1):
    for j in range(K+1-i):
        for k in range(K+1-i-j):
            if i+j+k==0:
                continue

            r = A*(2**i)
            g = B*(2**j)
            b = C*(2**k)
            if check(r, g, b):
                print("Yes")
                exit()

print("No")
