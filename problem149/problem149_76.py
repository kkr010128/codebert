import sys
N, M, X = map(int, sys.stdin.readline().split())
D = 12*100001
m = D
Clst = []

for i in range(N):
    Ci = list(map(int, sys.stdin.readline().split()))
    Clst.append(Ci)

for i in range(2**N):
    ch = True
    buy = []
    total = 0
    for j in range(N):
        if ((i>>j)&1):
            buy.append(Clst[j])
            total += Clst[j][0]
            if total >= m:
                ch = False
                break

    if ch:
        for l in range(1,M+1):
            skill = 0
            for k in buy:
                skill = skill + k[l]

            if skill < X:
                ch = False
                break
    
    if ch:
        m = total
    

if m == D:
    print(-1)
else:
    print(m)