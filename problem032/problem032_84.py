# coding: utf-8
n = int(input())

x = [float(i) for i in input().split()]
y = [float(i) for i in input().split()]

dl = [abs(i - j) for (i,j) in zip(x,y)]

for p in range(1,4):
    d = sum([i ** p for i in dl]) ** (1/p)
    print("{:.8f}".format(d))

print("{:.8f}".format(max(dl)))