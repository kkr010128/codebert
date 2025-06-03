import sys
import math

N = int(input())
A = map(int, input().split())
s = [0] * N
for a in A:
    s[a-1] += 1

for i in range(N):
    print(s[i])
