import sys
import math

lines = sys.stdin.readlines()
# print(lines)
n = int(lines[0].rstrip())
heights = [int(x) for x in lines[1].rstrip().split()]
# print(heights)
tot = 0
for i in range(n-1):
    if heights[i] <= heights[i+1]:
        continue
    else:
        diff = heights[i] - heights[i+1]
        heights[i+1] += diff
        tot += diff

print(tot)