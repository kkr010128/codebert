n = int(input())
xy = [list(map(int,input().split())) for i in range(n)]

from itertools import permutations
import math
m = math.factorial(n)
per = permutations(xy,n)

d = 0
c = 0
for j in per :
    for i in range(n-1):
        d += ((j[i+1][0]-j[i][0])**2 + (j[i+1][1]-j[i][1])**2) ** 0.5

print(d/m)
