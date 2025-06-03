import sys
from sys import stdin
input = stdin.readline
import math

th = math.pi/3.000000000000000

n = int(input())

p1 = [0.0000000000000000,0.00000000000000000]
p2 = [100.0000000000000,0.00000000000000000]

def koch(n,p1,p2):
    if n == 0:
        return
    s =[0,0]
    t =[0,0]
    u =[0,0]

    s[0] = (2.0 * p1[0] +1.0 * p2[0]) / 3.0
    s[1] = (2.0 * p1[1] +1.0 * p2[1]) / 3.0
    t[0] = (1.0 * p1[0] +2.0 * p2[0]) / 3.0
    t[1] = (1.0 * p1[1] +2.0 * p2[1]) / 3.0
    u[0] = (t[0] - s[0]) * math.cos(th) - (t[1] - s[1]) * math.sin(th) + s[0]
    u[1] = (t[0] - s[0]) * math.sin(th) + (t[1] - s[1]) * math.cos(th) + s[1]
      # p1,p2からs,t,uの座標を計算
    koch(n-1, p1, s)
    print(s[0],s[1])
    koch(n-1, s, u)
    print(u[0],u[1])
    koch(n-1, u, t)
    print(t[0],t[1])
    koch(n-1, t, p2)

print(0,0)
koch(n,p1,p2)
print(100,0)

