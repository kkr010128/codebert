N = int(input())
P = list(map(int,input().split()))
P = sorted([(P[i],i) for i in range(N)],key=lambda x:x[0])
cnt = 1
imin = P[0][1]
for i in range(1,N):
    ind = P[i][1]
    if ind<imin:
        cnt += 1
        imin = ind
print(cnt)