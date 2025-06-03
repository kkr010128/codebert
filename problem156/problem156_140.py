import sys
input = sys.stdin.readline
from collections import defaultdict

x = int(input())
pre = [i ** 5 for i in range(1001)] # Fuck it
for i in range(1001):
    for j in range(i + 1):
        if pre[i] - pre[j] == x: print(i, j); exit()
        elif pre[i] + pre[j] == x: print(i, -j); exit()
