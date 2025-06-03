N,M = map(int,input().split())
ls2 = []
for i in range(M):
    A,B = map(str,input().split())
    ls = [int(A)-1,B]
    ls2.append(ls)

Pena = 0
corr = 0

#ls3 = sorted(ls2, key=lambda x: x[0])
lsans = [[] for i in range(N)]
for i in range(M):
    lsans[ls2[i][0]].append(ls2[i][1])

for i in range(N):
    if 'AC' in lsans[i]:
        for ans in lsans[i]:
            if ans == 'WA':
                Pena += 1
            if ans == 'AC':
                corr += 1
                break
print(corr,Pena)