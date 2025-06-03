from itertools import combinations_with_replacement
CList = []
N, M, Q = map(int, input().split())
for i in range(1, M+1):
    CList.append(i)
Qtotal = []
x = 0
ans = 0

CList=list(combinations_with_replacement(CList, N))

a, b, c, d = map(int, input().split())
for i in CList:
    if CList[x][b-1]-CList[x][a-1] == c:
        Qtotal.append(d)
    else:
        Qtotal.append(0)
    x = x+1
x=0
for i in range(Q-1):
    a, b, c, d = map(int, input().split())
    for j in CList:
        if CList[x][b-1]-CList[x][a-1] == c:
            Qtotal[x] = Qtotal[x]+d
        x = x+1
    x=0

ans=max(Qtotal)
print(ans)
