N,M = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(M)]
n = -1
for x in range(1000):
    x = str(x)
    if len(x)!=N:continue
    ind = 0
    for i in range(M):
        s,c = A[i]
        if x[int(s)-1]!=str(c):
            ind=1
            break
    if ind==0:
        n = x
        break
print(n)