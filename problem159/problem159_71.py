import sys

X = int(input())
a = 100
d = 0
while(a<X):
    a = a * 101 // 100
    d += 1

print(d)
