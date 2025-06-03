import math
N = int(input())
num = list(map(int, input().split()))
#N = 10**6
#num = list(range(1, N+1))

MAXX = 10**6 + 1
MAXZ = int(math.sqrt(MAXX)+2)
furui = [[] for _ in range(MAXX)]

furui[1].append(1)
count = [0]*MAXX
for i in range(2, MAXX):
    if len(furui[i]) == 0:
        for k in range(i, MAXX, i):
            furui[k].append(i)

setwise = True
pairwise = True
for i in range(N):
    if not setwise and not pairwise: break
    for fu in furui[num[i]]:
        count[fu] += 1
        if fu > 1 and count[fu] >= N:
            setwise = False
            pairwise = False
            break
        elif fu > 1 and count[fu] > 1:
            pairwise = False

if pairwise:
    print('pairwise coprime')
elif setwise:
    print('setwise coprime')
else:
    print('not coprime')
