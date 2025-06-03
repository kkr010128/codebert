from sys import stdin
import sys

a = stdin.readline().rstrip()
b = stdin.readline().rstrip()

count = 0
for i in range(len(a)):
    if a[i] != b[i]: count = count + 1

print (count)

