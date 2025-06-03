import sys
import bisect

N = int(input())
a = list(map(int,input().split()))
numdic = {}
for i, num in enumerate(a):
    if num not in numdic:
        numdic[num] = [i+1]
    else:
        numdic[num].append(i+1)

if 1 not in numdic:
    print(-1)
    sys.exit()

nowplace = 0
count = 0
for i in range(1,N+1):
    if i not in numdic:
        break
    else:
        place = bisect.bisect_right(numdic[i], nowplace)
        if place >= len(numdic[i]):
            break
        else:
            nowplace = numdic[i][place]
            count += 1

print(N-count)