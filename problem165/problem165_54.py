from sys import stdin
import sys, math

n = int(stdin.readline().rstrip())

s = set()

for i in range(n):
    s.add(stdin.readline().rstrip())

print(len(s))

