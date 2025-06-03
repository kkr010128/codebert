# coding: utf-8
# Your code here!

x1, y1, x2, y2 = map(float,input().split())
x = (x2 - x1)
y = (y2 - y1)
s = (x*x + y*y)**(1/2)
print(s)
