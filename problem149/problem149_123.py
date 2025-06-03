from sys import stdin
import sys, math

n,m,x = [int(x) for x in stdin.readline().rstrip().split()]

c = []
for i in range(n):
    c.append([int(x) for x in stdin.readline().rstrip().split()])

money = []
for i in range(2**n):
    b = bin(i)
    d = [0 for i in range(m + 1)]
    for j in range(n):
        if b[-1] == "1": d = [p+q for (p,q) in zip(d,c[j])]
        b = str(bin(int(b, 2) // 2))

    if min(d[1:]) >= x: money.append(d[0])

if len(money) == 0:
    print(-1)
else:
    print(min(money))
   