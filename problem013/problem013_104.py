import sys

n = int(input())

dif_max = -float("inf")
min_v = float("inf")

for i in range(n):
    r = int(sys.stdin.readline())
    dif_max = max(dif_max, r - min_v)
    min_v = min(min_v, r)

print(dif_max)