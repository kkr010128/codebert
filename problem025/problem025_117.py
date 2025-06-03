# -*- coding: utf-8 -*-
n = int(input())
A = [int(n) for n in input().split()]
q = int(input())
M = [int(n) for n in input().split()]

numbers = [0]

for a in A:
    numbers = numbers + [n+a for n in numbers]

for m in M:
    if m in numbers:
        print("yes")
    else:
        print("no")