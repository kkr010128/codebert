# coding: utf-8
# Your code here!

import math

n = int(input())

p1 = [0.0, 0.0]
p2 = [100.0, 0.0]

def rad(r) :
    return math.radians(r)

def sin(s) :
    return math.sin(s)
    
def cos(s) :
    return math.cos(s)

def A(n, p1, p2) :
    if n == 0 :
        return 0
    else :
        s = [0, 0]
        t = [0, 0]
        u = [0, 0]
        
        s[0] = (p2[0] - p1[0]) / 3 + p1[0]
        s[1] = (p2[1] - p1[1]) / 3 + p1[1]
        t[0] = (p2[0] - p1[0]) / 3 * 2 + p1[0]
        t[1] = (p2[1] - p1[1]) / 3 * 2 + p1[1]
        
        u[0] = (t[0] - s[0]) * cos(rad(60)) - (t[1] - s[1]) * sin(rad(60)) + s[0]
        u[1] = (t[0] - s[0]) * sin(rad(60)) + (t[1] - s[1]) * cos(rad(60)) + s[1]
        
        A(n - 1, p1, s)
        p(s[0], s[1])
        
        A(n - 1, s, u)
        p(u[0], u[1])
        
        A(n - 1, u, t)
        p(t[0], t[1])
        
        A(n - 1, t, p2)
        
def p(x, y) :
    print(f"{x:.8f} {y:.8f}")
    
print(p1[0], p1[1])
A(n, p1, p2)
print(p2[0], p2[1])
