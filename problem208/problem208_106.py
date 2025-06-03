N, M = list(map(int,input().split()))
e = True
c = [-1 for i in range(N)]
for i in range(M):
    si, ci = list(map(int,input().split()))
    if c[si-1]>-1 and c[si-1]!=ci:
        e = False
    c[si-1] = ci
if e and (N==1 or c[0]!=0):
    print(max(0 if N==1 else 1, c[0]),end="")
    for i in range(1,N):
        print(max(0,c[i]),end="")
    print()
else:
    print(-1)