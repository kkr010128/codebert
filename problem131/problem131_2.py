# -*- coding: utf-8 -*-
a, v = map(int,input().split())
b, w = map(int,input().split())
t = int(input())

if a == b:
    print("YES")
    exit()

if v <= w:
    print("NO")
    exit()

#print(b-a, w-v, t*(w-v))
if a < b:
    if (b - a) <= t * (v - w): #(b - a) // (w - v) <= t
        print("YES")
    else:
        print("NO")
elif a > b:
    if (a - b) <= t * (v - w): #(a - b) // (v - w) <= t
        print("YES")
    else:
        print("NO")
