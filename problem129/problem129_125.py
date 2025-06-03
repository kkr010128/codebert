import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

a.sort()
tf = [True] * a[-1]
dup = [False] * a[-1]


for i in range(n):
    if tf[a[i]-1] == True:
        #print(a[i])
        if dup[a[i]-1] == True:
            tf[a[i]-1] = False
        else:
            dup[a[i]-1] = True
            for j in range(a[i]*2, a[-1]+1, a[i]):
                tf[j-1] = False
                

c = 0

#print(tf)

for x in a:
    if tf[x-1]:
        c += 1

print(c)






