N = int(input())
X = [list(map(int,input().split())) for _ in range(N)]
A = []
for i in range(N):
    x,l = X[i]
    A.append((x-l,x+l))
B1 = sorted(A,key=lambda x:x[1])
B1 = [(B1[i][0],B1[i][1],i) for i in range(N)]
B2 = sorted(B1,key=lambda x:x[0])
hist = [0 for _ in range(N)]
cnt = 0
i = 0
for k in range(N):
    if hist[k]==0:
        r = B1[k][1]
        hist[k] = 1
        cnt += 1
        while i<N:
            l,j = B2[i][0],B2[i][2]
            if hist[j]==1:
                i += 1
                continue
            if l<r:
                hist[j] = 1
                i += 1
            else:
                break
print(cnt)