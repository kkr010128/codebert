from math import log10

n = int(input())

if n % 2:
    print(0)
    exit(0)

n -= n % 10
s = n // 10
t = s

while t != 0:
    s += t // 5
    t //= 5

print(s)