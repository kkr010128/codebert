from itertools import permutations
import math
N = int(input())
l = [list(map(int, input().split())) for i in range(N)]

waru = 1
for i in range(N):
    waru*= i+1
a = [i+1 for i in range(N)]
c = 0
su = 0
for i in permutations(a,N):
    li = list(i)
    for j in range(len(li)-1):
        start = l[li[j]-1]
        g = l[li[j+1]-1]
        su += math.sqrt((start[0]-g[0]) ** 2 + (start[1]-g[1]) ** 2)
print(su/waru)