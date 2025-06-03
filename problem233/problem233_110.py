#41
import math
N = int(input())
p = list(map(int,input().split()))

cou = 0
x = math.inf

for j in range(N):
    if min(x,p[j]) == p[j]:
        x = p[j]
        cou += 1

print(cou)

