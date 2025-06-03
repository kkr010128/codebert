from operator import itemgetter

N,M = map(int,input().split())
PS = [list(map(str,input().split())) for i in range(M)]

for i in range(M) :
    PS[i][0] = int(PS[i][0])

submits = [["null"] for i in range(N)]
for i in range(M) :
    submits[PS[i][0]-1][0] = PS[i][0]-1
    submits[PS[i][0]-1].append(PS[i][1])

ac = 0
pena = 0
for i in range(len(submits)) :
    if submits[i][0] == "null" :
        continue

    flag = False
    wabuf1 = 0
    for j in range(1,len(submits[i])) :
        if submits[i][j] == "AC" :
            ac += 1
            flag = True
            break
        else :
            wabuf1 += 1
    if flag == True :
        pena += wabuf1

print(ac,pena)