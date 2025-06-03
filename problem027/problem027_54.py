import math
from math import cos, sin, pi

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

def koch(n,a,b):
  if n == 0:
    return 0

  th = pi * 60.0 / 180.0

  s, t, u = Point(0.0, 0.0), Point(0.0, 0.0), Point(0.0, 0.0)

  s.x = (2.0 * a.x + 1.0 * b.x) / 3.0
  s.y = (2.0 * a.y + 1.0 * b.y) / 3.0
  t.x = (1.0 * a.x + 2.0 * b.x) / 3.0
  t.y = (1.0 * a.y + 2.0 * b.y) / 3.0
  u.x = (t.x - s.x) * cos(th) - (t.y - s.y) * sin(th) + s.x
  u.y = (t.x - s.x) * sin(th) + (t.y - s.y) * cos(th) + s.y

  koch(n - 1, a, s)
  print(f'{s.x:,.8f} {s.y:,.8f}')

  koch(n - 1, s, u)
  print(f'{u.x:,.8f} {u.y:,.8f}')
  
  koch(n - 1, u, t)
  print(f'{t.x:,.8f} {t.y:,.8f}')

  koch(n - 1, t, b)
    

a = Point(0.0, 0.0)
b = Point(100.0, 0.0)
n = int(input())

print(f'{a.x:,.8f} {a.y:,.8f}')
koch(n,a,b)
print(f'{b.x:,.8f} {b.y:,.8f}')
