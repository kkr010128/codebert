#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [input() for _ in range(n)]

import itertools
import math
n = int(input())
l = [list(map(int,input().split())) for i in range(n)]


seq = []
for i in range(n):
    seq.append(i)

a = list(itertools.permutations(seq))
#print(a)

ans = 0
for i in a:
    for j in range(0,n-1):
        #idx1とidx2との距離
        ans += math.sqrt((l[i[j]][0] - l[i[j+1]][0])**2 + (l[i[j]][1] - l[i[j+1]][1])**2)


print(ans/len(a))

