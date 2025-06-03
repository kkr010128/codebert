import statistics
import math

N = int(input())
A_B = [[int(i) for i in input().split(' ')] for n in range(N)]

t = list(zip(*A_B))

A_sta = statistics.median(t[0])
B_sta = statistics.median(t[1])

if N % 2 == 0:
    count = int(2 * (B_sta - A_sta) + 1)
else:
    count = B_sta - A_sta + 1

print(count)